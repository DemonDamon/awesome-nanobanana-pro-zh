#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nano Banana Pro 风格迁移提示词生成器

使用阿里云百炼的 qwen-vl-plus 多模态大模型，根据输入图片和目标风格，
自动生成适用于 Nano Banana Pro 的风格迁移提示词。

使用方法:
    python style_transfer.py --image <图片路径或URL> --style <风格名称>

示例:
    python style_transfer.py --image photo.jpg --style "电影感风格"
    python style_transfer.py --image https://example.com/image.jpg --style "水彩画风格"
"""

import os
import sys
import argparse
import base64
from pathlib import Path
from openai import OpenAI


# 预定义的风格模板
STYLE_TEMPLATES = {
    "电影感风格": """cinematic shot, dramatic lighting, epic composition, wide-angle lens (35mm), shallow depth of field with beautiful bokeh, professional color grading with moody tones, high dynamic range (HDR), subtle film grain, 8K resolution, photorealistic, creating a sense of drama and epicness.""",
    
    "水彩画风格": """watercolor painting style, soft and translucent colors, visible brush strokes and water bleeds, wet-on-wet technique, beautiful color gradients, highlights showing the white paper texture, capturing the luminous and spontaneous nature of watercolor art. The overall mood is dreamy and serene.""",
    
    "赛博朋克风格": """cyberpunk style, futuristic cityscape at night, drenched in neon lights and holographic advertisements. Towering skyscrapers, flying vehicles, and streets filled with augmented reality elements. A dense, rainy atmosphere with reflective wet pavements. Color palette dominated by electric blues, vibrant pinks, and deep purples. High contrast, dystopian mood, reminiscent of Blade Runner aesthetics. 8K, ultra-detailed.""",
    
    "日式动漫风格": """Japanese anime style, vibrant and cel-shaded colors, clean and sharp line art, expressive characters with large eyes and detailed hair. The background is beautifully painted, reminiscent of Studio Ghibli/Makoto Shinkai style. Dynamic composition with a sense of motion and emotion. 2D anime aesthetic, high quality, 8K resolution.""",
    
    "梵高油画风格": """In the style of Vincent van Gogh's oil painting. Thick, impasto brushstrokes with visible texture, swirling and expressive lines, and a vibrant, emotional color palette. The light is dynamic and almost alive, with a strong sense of movement and feeling. Post-Impressionist aesthetic, capturing the artist's subjective experience.""",
    
    "低多边形风格": """low poly style, a 3D render composed of visible geometric polygons. Simplified and faceted shapes, clean edges, and a vibrant, minimalist color palette. The lighting is often simple, emphasizing the geometric forms. The overall look is a blend of digital abstraction and representational art. Isometric view, high resolution.""",
}


def encode_image_to_base64(image_path: str) -> str:
    """将本地图片编码为 base64 字符串"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def is_url(path: str) -> bool:
    """判断是否为 URL"""
    return path.startswith(('http://', 'https://'))


def analyze_image_content(client: OpenAI, image_input: str) -> str:
    """
    使用 qwen-vl-plus 分析图片内容
    
    Args:
        client: OpenAI 客户端实例
        image_input: 图片 URL 或本地路径
    
    Returns:
        图片内容的详细描述
    """
    # 准备图片输入
    if is_url(image_input):
        image_data = {"url": image_input}
    else:
        # 本地文件，使用 base64 编码
        base64_image = encode_image_to_base64(image_input)
        image_data = {"url": f"data:image/jpeg;base64,{base64_image}"}
    
    # 调用模型分析图片
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": image_data,
                    },
                    {
                        "type": "text",
                        "text": """请详细描述这张图片的内容，包括：
1. 主要对象和场景
2. 构图和视角
3. 光线和氛围
4. 色彩特征
5. 任何值得注意的细节

请用英文回答，使用简洁专业的描述语言，适合用于图像生成提示词。"""
                    },
                ],
            },
        ],
    )
    
    return completion.choices[0].message.content


def generate_style_transfer_prompt(
    client: OpenAI,
    image_input: str,
    style_name: str,
    custom_style: str = None
) -> dict:
    """
    生成风格迁移提示词
    
    Args:
        client: OpenAI 客户端实例
        image_input: 图片 URL 或本地路径
        style_name: 目标风格名称
        custom_style: 自定义风格描述（可选）
    
    Returns:
        包含内容描述、风格模板和完整提示词的字典
    """
    print(f"🔍 正在分析图片内容...")
    content_description = analyze_image_content(client, image_input)
    print(f"✅ 图片内容分析完成\n")
    
    # 获取风格模板
    if custom_style:
        style_template = custom_style
    elif style_name in STYLE_TEMPLATES:
        style_template = STYLE_TEMPLATES[style_name]
    else:
        print(f"⚠️  未找到预定义风格 '{style_name}'，将使用自定义风格生成")
        style_template = style_name
    
    print(f"🎨 正在生成风格迁移提示词...")
    
    # 准备图片输入
    if is_url(image_input):
        image_data = {"url": image_input}
    else:
        base64_image = encode_image_to_base64(image_input)
        image_data = {"url": f"data:image/jpeg;base64,{base64_image}"}
    
    # 使用 VL 模型生成完整提示词
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": image_data,
                    },
                    {
                        "type": "text",
                        "text": f"""我想将这张图片的内容用以下风格重新生成：

【目标风格】
{style_template}

【任务】
请基于图片的实际内容和上述风格要求，生成一个完整的、适用于 Nano Banana Pro 图像生成模型的提示词。

【要求】
1. 提示词必须用英文
2. 首先描述图片中的具体内容（主体、场景、构图等）
3. 然后融入上述风格的所有特征
4. 确保提示词详细、具体、结构清晰
5. 适合直接用于 Nano Banana Pro 模型生成图像

请直接输出完整的提示词，不需要额外解释。"""
                    },
                ],
            },
        ],
    )
    
    final_prompt = completion.choices[0].message.content
    print(f"✅ 风格迁移提示词生成完成\n")
    
    return {
        "content_description": content_description,
        "style_template": style_template,
        "final_prompt": final_prompt,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Nano Banana Pro 风格迁移提示词生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --image photo.jpg --style "电影感风格"
  %(prog)s --image https://example.com/image.jpg --style "水彩画风格"
  %(prog)s --image photo.jpg --custom-style "impressionist painting with soft brushstrokes"

可用的预定义风格:
  - 电影感风格
  - 水彩画风格
  - 赛博朋克风格
  - 日式动漫风格
  - 梵高油画风格
  - 低多边形风格
        """
    )
    
    parser.add_argument(
        "--image",
        required=True,
        help="输入图片路径（本地文件或 URL）"
    )
    
    parser.add_argument(
        "--style",
        help="目标风格名称（从预定义风格中选择）"
    )
    
    parser.add_argument(
        "--custom-style",
        help="自定义风格描述（英文）"
    )
    
    parser.add_argument(
        "--api-key",
        help="阿里云百炼 API Key（也可通过环境变量 DASHSCOPE_API_KEY 设置）"
    )
    
    parser.add_argument(
        "--output",
        help="输出文件路径（可选，默认输出到终端）"
    )
    
    args = parser.parse_args()
    
    # 验证参数
    if not args.style and not args.custom_style:
        parser.error("必须指定 --style 或 --custom-style 之一")
    
    # 获取 API Key
    api_key = args.api_key or os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        print("❌ 错误: 未找到 API Key")
        print("请通过 --api-key 参数或 DASHSCOPE_API_KEY 环境变量提供")
        print("\n获取 API Key: https://help.aliyun.com/zh/model-studio/get-api-key")
        sys.exit(1)
    
    # 验证图片路径
    if not is_url(args.image) and not Path(args.image).exists():
        print(f"❌ 错误: 图片文件不存在: {args.image}")
        sys.exit(1)
    
    # 初始化客户端
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    
    print("=" * 70)
    print("🍌 Nano Banana Pro 风格迁移提示词生成器")
    print("=" * 70)
    print(f"📷 输入图片: {args.image}")
    print(f"🎨 目标风格: {args.style or '自定义风格'}")
    print("=" * 70)
    print()
    
    # 生成提示词
    try:
        result = generate_style_transfer_prompt(
            client=client,
            image_input=args.image,
            style_name=args.style or "",
            custom_style=args.custom_style
        )
        
        # 格式化输出
        output_text = f"""{'=' * 70}
📋 图片内容分析
{'=' * 70}

{result['content_description']}

{'=' * 70}
🎨 风格模板
{'=' * 70}

{result['style_template']}

{'=' * 70}
✨ 完整提示词（可直接用于 Nano Banana Pro）
{'=' * 70}

{result['final_prompt']}

{'=' * 70}
"""
        
        # 输出结果
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"✅ 结果已保存到: {args.output}")
        else:
            print(output_text)
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
