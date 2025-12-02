# Awesome Nano Banana Pro (中文版) 🍌

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选的 Nano Banana Pro 提示词、图像生成风格和资源集合，助您掌握提示词工程，探索 Nano Banana Pro AI 图像模型的创意潜力。

本仓库专注于高保真图像提示词，其灵感来源于 X (Twitter)、微信、Replicate 和顶级的提示词工程师。无论您是想生成逼真的肖像、风格化的美学图片，还是进行复杂的创意实验，这里都有最有效的输入方式，助您释放模型的全部潜能。

---

## 📖 目录

1.  [照片编辑与特效](#1-照片编辑与特效)
2.  [创意场景生成](#2-创意场景生成)
3.  [人物肖像与风格](#3-人物肖像与风格)
4.  [科幻与奇幻](#4-科幻与奇幻)
5.  [产品与商业](#5-产品与商业)
6.  [建筑与室内](#6-建筑与室内)
7.  [艺术与插画](#7-艺术与插画)
8.  [贡献指南](#8-贡献指南)

---

## 1. 照片编辑与特效

### 1.1. 移除背景并替换

此提示词可用于移除图像背景，并替换为纯色或渐变色，适合用于制作证件照或产品图。

**提示词:**

```
Remove the background of the uploaded image and replace it with a solid white color. Keep the main subject in sharp focus.
```

**效果图 (占位):**

![placeholder](https://via.placeholder.com/512x512.png?text=替换背景后)

---

## 2. 创意场景生成

### 2.1. 外星人入侵与超级英雄救援

这是一个复杂的场景，融合了图像编辑、角色添加和氛围营造，非常适合测试模型的多任务处理能力。

**原始图片:**

![original image](https://a.lovart.ai/artifacts/user/vc1FpRVyYtUzPipp.jpg)

**提示词:**

```
Based on the uploaded image, first, replace the light reflection on the window with alien spaceships in the sky, creating an atmosphere of an alien invasion. The image should maintain the original city skyline and bright sky, while adding a sense of sci-fi tension with the alien ships.

Next, add Iron Man outside the window, urgently shouting for evacuation. He is hanging upside down, with his face pressed against the glass, facing me. His left hand is knocking on the window, and his right hand is pointing at the alien ships, showing an anxious and urgent expression and gesture. Create a tense evacuation atmosphere.

Finally, add some explosions, fire, and smoke to the scene to enhance the sense of crisis. The overall style should remain realistic, consistent with the original image.
```

**效果图 (占位):**

![placeholder](https://via.placeholder.com/512x512.png?text=外星人入侵与钢铁侠)

**来源:** 用户提供的示例

---

## 3. 人物肖像与风格

### 3.1. 2000年代复古自拍

使用结构化的 JSON 提示词，生成具有闪光灯效果和怀旧元素的2000年代初风格自拍。

**提示词:**

```json
{
  "subject": {
    "description": "A young woman taking a mirror selfie with very long voluminous dark waves and soft wispy bangs",
    "age": "young adult",
    "expression": "confident and slightly playful"
  },
  "photography": {
    "camera_style": "early-2000s digital camera aesthetic",
    "lighting": "harsh super-flash with bright blown-out highlights but subject still visible"
  },
  "background": {
    "setting": "nostalgic early-2000s bedroom"
  }
}
```

**效果图 (占位):**

![placeholder](https://via.placeholder.com/512x512.png?text=2000年代复古自拍)

**来源:** @ZaraIrahh

---

## 8. 贡献指南

欢迎大家为这个项目做出贡献！

如果您有好的提示词案例，请通过以下方式贡献：

1.  **Fork** 本仓库
2.  创建一个新的分支 (`git checkout -b feature/YourAwesomePrompt`)
3.  在 `README.md` 中添加您的提示词案例
4.  提交您的修改 (`git commit -m 'Add some awesome prompt'`)
5.  推送到分支 (`git push origin feature/YourAwesomePrompt`)
6.  创建一个新的 Pull Request
