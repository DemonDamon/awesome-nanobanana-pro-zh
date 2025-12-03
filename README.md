# Awesome Nano Banana Pro (中文版) 🍌 - 风格化提示词集合

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

欢迎来到 Awesome Nano Banana Pro 中文版！这是一个专注于**风格化提示词**的精选集合，旨在帮助您轻松地将各种艺术风格应用于不同场景，释放 Nano Banana Pro 模型的全部创意潜能。

与场景导向的提示词不同，本仓库的核心是**风格的复用性**。我们提供模块化的风格提示词，您可以轻松地将其与具体的内容描述结合，生成独一无二的艺术作品。

> 💡 **核心理念**: `风格模板` + `内容描述` = `无限创意`

---

## 🚀 新功能：AI 风格迁移脚本

为了进一步提升您的创作效率，我们开发了一个 Python 脚本，可以调用阿里云百炼的多模态大模型 `qwen-vl-plus`，根据您提供的一张图片和一个目标风格，自动生成详细的风格迁移提示词。

### 快速开始

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 配置 API Key

获取阿里云百炼 API Key：https://help.aliyun.com/zh/model-studio/get-api-key

配置环境变量：

```bash
export DASHSCOPE_API_KEY="sk-your-api-key-here"
```

或者在运行时通过 `--api-key` 参数指定。

#### 3. 运行脚本

**使用预定义风格：**

```bash
python style_transfer.py --image your_photo.jpg --style "电影感风格"
```

**使用自定义风格：**

```bash
python style_transfer.py --image your_photo.jpg --custom-style "impressionist painting with soft pastel colors"
```

**保存结果到文件：**

```bash
python style_transfer.py --image your_photo.jpg --style "水彩画风格" --output result.txt
```

### 脚本功能

- ✅ **自动分析图片内容**：使用 VL 模型理解图片中的主体、场景、构图、光线等元素
- ✅ **智能融合风格**：将图片内容与目标风格模板智能结合
- ✅ **生成完整提示词**：输出可直接用于 Nano Banana Pro 的高质量提示词
- ✅ **支持本地图片和 URL**：灵活的输入方式
- ✅ **预定义 6 种风格**：电影感、水彩画、赛博朋克、日式动漫、梵高油画、低多边形
- ✅ **支持自定义风格**：可以输入任何风格描述

### 使用示例

假设您有一张城市街景照片，想要转换为赛博朋克风格：

```bash
python style_transfer.py --image city_street.jpg --style "赛博朋克风格"
```

脚本会：
1. 分析图片内容（街道、建筑、行人等）
2. 应用赛博朋克风格特征（霓虹灯、未来感、雨夜氛围等）
3. 生成完整提示词，例如：

```
A bustling city street at night transformed into a cyberpunk dystopia. 
The street is lined with towering skyscrapers covered in massive holographic 
advertisements and neon signs in Japanese and English. The wet pavement 
reflects the vibrant colors - electric blues, hot pinks, and deep purples. 
Flying vehicles navigate between buildings while pedestrians with augmented 
reality implants walk through the dense, rainy atmosphere. High contrast, 
dystopian mood, reminiscent of Blade Runner aesthetics. 8K, ultra-detailed.
```

---

## 🎨 风格目录

1.  [**电影感风格 (Cinematic Style)**](#1-电影感风格-cinematic-style)
2.  [**水彩画风格 (Watercolor Style)**](#2-水彩画风格-watercolor-style)
3.  [**赛博朋克风格 (Cyberpunk Style)**](#3-赛博朋克风格-cyberpunk-style)
4.  [**日式动漫风格 (Anime Style)**](#4-日式动漫风格-anime-style)
5.  [**梵高油画风格 (Van Gogh Oil Painting Style)**](#5-梵高油画风格-van-gogh-oil-painting-style)
6.  [**低多边形风格 (Low Poly Style)**](#6-低多边形风格-low-poly-style)
7.  [**贡献指南**](#7-贡献指南)

---

## 1. 电影感风格 (Cinematic Style)

营造电影大片的视觉质感，强调光影、氛围和故事感。适合需要戏剧性、史诗感或情绪渲染的场景。

### 风格模板

```
cinematic shot, dramatic lighting, epic composition, wide-angle lens (35mm), shallow depth of field with beautiful bokeh, professional color grading with [moody tones/vibrant colors/desaturated look], high dynamic range (HDR), subtle film grain, 8K resolution, photorealistic, creating a sense of [drama/mystery/epicness].
```

**使用说明**：将 `[moody tones/vibrant colors/desaturated look]` 替换为您想要的色调风格，将 `[drama/mystery/epicness]` 替换为您想要传达的情绪。

### 场景示例

#### 示例 1: 城市雨夜

**内容描述**: `A lone detective standing on a wet city street at night, illuminated by neon signs.`

**完整提示词**:
```
cinematic shot of a lone detective standing on a wet city street at night, illuminated by neon signs. dramatic lighting, epic composition, wide-angle lens (35mm), shallow depth of field with beautiful bokeh, professional color grading with moody tones, high dynamic range (HDR), subtle film grain, 8K resolution, photorealistic, creating a sense of mystery.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 沙漠日落

**内容描述**: `A caravan of camels walking across sand dunes at sunset.`

**完整提示词**:
```
cinematic shot of a caravan of camels walking across sand dunes at sunset. dramatic lighting with long shadows, epic composition, wide-angle lens (35mm), shallow depth of field with beautiful bokeh, professional color grading with vibrant orange and purple colors, high dynamic range (HDR), subtle film grain, 8K resolution, photorealistic, creating a sense of epic journey.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 战场废墟

**内容描述**: `A soldier standing among ruins of a destroyed building, dust and smoke in the air.`

**完整提示词**:
```
cinematic shot of a soldier standing among ruins of a destroyed building, dust and smoke in the air. dramatic lighting with rays of sunlight breaking through the debris, epic composition, wide-angle lens (35mm), shallow depth of field with beautiful bokeh, professional color grading with desaturated look and muted colors, high dynamic range (HDR), subtle film grain, 8K resolution, photorealistic, creating a sense of drama and loss.
```

**效果图**: *(待测试后添加)*

---

## 2. 水彩画风格 (Watercolor Style)

模拟水彩画的通透、流动和柔和的质感。适合需要柔美、梦幻或自然感的场景。

### 风格模板

```
watercolor painting style, soft and translucent colors, visible brush strokes and water bleeds, wet-on-wet technique, beautiful color gradients, highlights showing the white paper texture, capturing the luminous and spontaneous nature of watercolor art. The overall mood is [dreamy/serene/vibrant].
```

**使用说明**：将 `[dreamy/serene/vibrant]` 替换为您想要的氛围。

### 场景示例

#### 示例 1: 乡村风景

**内容描述**: `A rustic cottage surrounded by a field of wildflowers.`

**完整提示词**:
```
watercolor painting style of a rustic cottage surrounded by a field of wildflowers. soft and translucent colors, visible brush strokes and water bleeds, wet-on-wet technique, beautiful color gradients, highlights showing the white paper texture, capturing the luminous and spontaneous nature of watercolor art. The overall mood is serene.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 街边咖啡馆

**内容描述**: `A charming street-side cafe with people enjoying coffee.`

**完整提示词**:
```
watercolor painting style of a charming street-side cafe with people enjoying coffee. soft and translucent colors, visible brush strokes and water bleeds, wet-on-wet technique, beautiful color gradients, highlights showing the white paper texture, capturing the luminous and spontaneous nature of watercolor art. The overall mood is vibrant and lively.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 海边日出

**内容描述**: `A peaceful beach at sunrise with gentle waves and seabirds.`

**完整提示词**:
```
watercolor painting style of a peaceful beach at sunrise with gentle waves and seabirds. soft and translucent colors with warm oranges and pinks in the sky, visible brush strokes and water bleeds, wet-on-wet technique, beautiful color gradients, highlights showing the white paper texture, capturing the luminous and spontaneous nature of watercolor art. The overall mood is dreamy and tranquil.
```

**效果图**: *(待测试后添加)*

---

## 3. 赛博朋克风格 (Cyberpunk Style)

高科技、低生活的未来主义风格，以霓虹灯、机械改造和反乌托邦氛围为特征。适合科幻、未来城市或技术主题的场景。

### 风格模板

```
cyberpunk style, futuristic cityscape at night, drenched in neon lights and holographic advertisements. Towering skyscrapers, flying vehicles, and streets filled with augmented reality elements. A dense, rainy atmosphere with reflective wet pavements. Color palette dominated by electric blues, vibrant pinks, and deep purples. High contrast, dystopian mood, reminiscent of Blade Runner aesthetics. 8K, ultra-detailed.
```

### 场景示例

#### 示例 1: 机械义体维修店

**内容描述**: `A mechanic working on a complex robotic arm in a cluttered workshop.`

**完整提示词**:
```
cyberpunk style, a mechanic working on a complex robotic arm in a cluttered workshop. The scene is drenched in neon lights from outside signs and holographic advertisements. The workshop is filled with tools, wires, and spare parts. A dense, rainy atmosphere is visible through the window. Color palette dominated by electric blues, vibrant pinks, and deep purples. High contrast, dystopian mood, 8K, ultra-detailed.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 数据黑客的藏身处

**内容描述**: `A data hacker surrounded by multiple holographic screens in a hidden underground base.`

**完整提示词**:
```
cyberpunk style, a data hacker surrounded by multiple glowing holographic screens in a hidden underground base. The room is dark, only lit by the data streams and interfaces on the screens. Wires and cables run across the floor and ceiling. Color palette dominated by electric blues, vibrant greens, and deep purples. High contrast, intense and focused mood, 8K, ultra-detailed.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 空中交通枢纽

**内容描述**: `A busy aerial traffic hub with flying cars and drones at different levels.`

**完整提示词**:
```
cyberpunk style, a busy aerial traffic hub with flying cars and drones at different levels. Towering skyscrapers with massive holographic advertisements and neon signs. The scene is set at night with a dense, rainy atmosphere and reflective wet surfaces on the landing platforms. Color palette dominated by electric blues, vibrant pinks, and deep purples. High contrast, dystopian mood, reminiscent of Blade Runner aesthetics. 8K, ultra-detailed.
```

**效果图**: *(待测试后添加)*

---

## 4. 日式动漫风格 (Anime Style)

模仿日本动漫的经典画风，线条清晰，色彩鲜明，人物具有标志性的特征。适合角色设计、故事场景或需要表现力的画面。

### 风格模板

```
Japanese anime style, vibrant and cel-shaded colors, clean and sharp line art, expressive characters with large eyes and detailed hair. The background is beautifully painted, reminiscent of [Studio Ghibli/Makoto Shinkai] style. Dynamic composition with a sense of motion and emotion. 2D anime aesthetic, high quality, 8K resolution.
```

**使用说明**：将 `[Studio Ghibli/Makoto Shinkai]` 替换为您喜欢的动漫风格参考。

### 场景示例

#### 示例 1: 樱花下的少女

**内容描述**: `A high school girl in a uniform standing under a blooming cherry blossom tree, with petals gently falling around her.`

**完整提示词**:
```
Japanese anime style, a high school girl in a uniform standing under a blooming cherry blossom tree, with petals gently falling around her. Vibrant and cel-shaded colors, clean and sharp line art, expressive character with large eyes and detailed hair. The background is beautifully painted, reminiscent of Makoto Shinkai style with soft lighting. Dynamic composition with a sense of emotion. 2D anime aesthetic, high quality, 8K resolution.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 东京街头的战斗

**内容描述**: `Two powerful warriors clashing with energy swords in the middle of a busy Tokyo street at night.`

**完整提示词**:
```
Japanese anime style, two powerful warriors clashing with energy swords in the middle of a busy Tokyo street at night. Vibrant and cel-shaded colors, clean and sharp line art, expressive characters with dynamic poses. The background is a detailed Tokyo cityscape with neon signs, reminiscent of classic sci-fi anime. Dynamic composition with a sense of intense motion and action. 2D anime aesthetic, high quality, 8K resolution.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 魔法学院的图书馆

**内容描述**: `A grand magical library with floating books and glowing magical circles.`

**完整提示词**:
```
Japanese anime style, a grand magical library with floating books and glowing magical circles. Vibrant and cel-shaded colors with warm lighting, clean and sharp line art. The background is beautifully painted with towering bookshelves and mystical details, reminiscent of Studio Ghibli style. Dynamic composition with a sense of wonder and magic. 2D anime aesthetic, high quality, 8K resolution.
```

**效果图**: *(待测试后添加)*

---

## 5. 梵高油画风格 (Van Gogh Oil Painting Style)

模仿梵高独特的笔触、厚重的颜料和充满情感的色彩。适合需要艺术感、表现力或情感强度的场景。

### 风格模板

```
In the style of Vincent van Gogh's oil painting. Thick, impasto brushstrokes with visible texture, swirling and expressive lines, and a vibrant, emotional color palette. The light is dynamic and almost alive, with a strong sense of movement and feeling. Post-Impressionist aesthetic, capturing the artist's subjective experience.
```

### 场景示例

#### 示例 1: 向日葵花田

**内容描述**: `A vast field of sunflowers under a bright, turbulent sky.`

**完整提示词**:
```
In the style of Vincent van Gogh's oil painting, a vast field of sunflowers under a bright, turbulent sky. Thick, impasto brushstrokes with visible texture, swirling and expressive lines defining the flowers and clouds, and a vibrant, emotional color palette of yellows, blues, and greens. The light is dynamic and almost alive, with a strong sense of movement and feeling. Post-Impressionist aesthetic.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 夜晚的咖啡馆露台

**内容描述**: `An outdoor cafe terrace at night, with gaslights casting a warm glow on the cobblestone street.`

**完整提示词**:
```
In the style of Vincent van Gogh's oil painting, an outdoor cafe terrace at night, with gaslights casting a warm glow on the cobblestone street. Thick, impasto brushstrokes with visible texture, swirling and expressive lines in the starry night sky, and a vibrant, emotional color palette contrasting warm yellows and oranges with deep blues. The light is dynamic and almost alive, with a strong sense of movement and feeling. Post-Impressionist aesthetic.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 麦田与乌鸦

**内容描述**: `A wheat field under a dramatic stormy sky with crows flying overhead.`

**完整提示词**:
```
In the style of Vincent van Gogh's oil painting, a wheat field under a dramatic stormy sky with crows flying overhead. Thick, impasto brushstrokes with visible texture, swirling and expressive lines in the turbulent clouds, and a vibrant, emotional color palette of golden yellows, deep blues, and blacks. The light is dynamic and almost alive, with a strong sense of movement and tension. Post-Impressionist aesthetic, capturing intense emotion.
```

**效果图**: *(待测试后添加)*

---

## 6. 低多边形风格 (Low Poly Style)

使用多边形网格来构建三维模型，形成一种独特的、数字化的几何美学。适合游戏美术、现代设计或需要简约几何感的场景。

### 风格模板

```
low poly style, a 3D render composed of visible geometric polygons. Simplified and faceted shapes, clean edges, and a vibrant, minimalist color palette. The lighting is often simple, emphasizing the geometric forms. The overall look is a blend of digital abstraction and representational art. Isometric view, high resolution.
```

### 场景示例

#### 示例 1: 漂浮的岛屿

**内容描述**: `A small, floating island with a single tree and a waterfall cascading down its side.`

**完整提示词**:
```
low poly style, a 3D render of a small, floating island with a single tree and a waterfall cascading down its side. The island, tree, and water are composed of visible geometric polygons. Simplified and faceted shapes, clean edges, and a vibrant, minimalist color palette of greens, blues, and browns. The lighting is simple, emphasizing the geometric forms. Isometric view, high resolution.
```

**效果图**: *(待测试后添加)*

---

#### 示例 2: 森林中的鹿

**内容描述**: `A majestic deer standing in a quiet forest clearing.`

**完整提示词**:
```
low poly style, a 3D render of a majestic deer standing in a quiet forest clearing. The deer and the surrounding trees are composed of visible geometric polygons. Simplified and faceted shapes, clean edges, and a vibrant, minimalist color palette of oranges, browns, and greens. The lighting is simple, emphasizing the geometric forms. Isometric view, high resolution.
```

**效果图**: *(待测试后添加)*

---

#### 示例 3: 山间小屋

**内容描述**: `A cozy cabin in the mountains surrounded by pine trees and snow.`

**完整提示词**:
```
low poly style, a 3D render of a cozy cabin in the mountains surrounded by pine trees and snow. The cabin, trees, and landscape are composed of visible geometric polygons. Simplified and faceted shapes, clean edges, and a vibrant, minimalist color palette of whites, blues, and greens. The lighting is simple, emphasizing the geometric forms. Isometric view, high resolution.
```

**效果图**: *(待测试后添加)*

---

## 7. 贡献指南

我们欢迎并感谢所有形式的贡献！如果您有优秀的风格提示词或改进建议，请通过以下方式分享：

### 如何贡献

1.  **Fork 本仓库**
2.  **创建新分支** (`git checkout -b feature/YourAwesomeStyle`)
3.  **添加你的内容** (在 README.md 中添加新的风格模板和示例)
4.  **提交更改** (`git commit -m "feat: Add YourAwesomeStyle"`)
5.  **推送到分支** (`git push origin feature/YourAwesomeStyle`)
6.  **创建 Pull Request**

### 贡献内容类型

- 🎨 **新的风格模板**：添加新的艺术风格和对应的提示词模板
- 📸 **场景示例**：为现有风格添加更多场景示例
- 🖼️ **效果图**：提供实际生成的图片作为参考
- 🐛 **Bug 修复**：修正提示词中的错误或改进表达
- 📚 **文档改进**：完善使用说明或添加教程

---

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

---

## 🙏 致谢

感谢所有为本项目贡献提示词和建议的朋友们！

特别感谢：
- 原版 [awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro) 项目的启发
- 阿里云百炼团队提供的优秀多模态大模型 API

---

## 📮 联系方式

如有问题或建议，欢迎通过 [Issues](https://github.com/DemonDamon/awesome-nanobanana-pro-zh/issues) 与我们交流。

---

**⭐ 如果这个项目对您有帮助，请给我们一个 Star！**
