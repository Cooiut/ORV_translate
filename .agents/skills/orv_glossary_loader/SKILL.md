---
name: orv_glossary_loader
description: 在开始翻译 ORV 外传章节前触发。扫描待翻译的源文件，从分层词汇表中提取本章相关词条，构建精简词汇上下文，避免全量词汇注入导致的注意力稀释。
---

# ORV 分层词汇加载器

## 触发时机
当用户指示翻译某一章节或某个 XHTML 文件时，**在开始翻译之前**执行以下流程。

---

## 执行步骤

### 第一步：加载核心词汇（必选）
读取 `.agents/glossary/core.md`，将其全部内容纳入本次翻译的词汇上下文。核心词汇无论章节内容如何，均需完整加载。

### 第二步：扫描源文件
读取待翻译的源 XHTML 文件，提取其中出现的英文词汇（专有名词、技能名、地点名等）。重点关注以下特征的词汇：
- 首字母大写的名词或名词短语
- 包含罗马音拼写的韩文名（如 `Hakhyun`, `Joonghyuk`）
- 带方括号的技能/系统名（如 `[Fourth Wall]`）

### 第三步：分类匹配
将扫描到的词汇与以下分类词汇表逐一比对：

| 词汇表文件 | 涵盖内容 |
|---|---|
| `.agents/glossary/characters.md` | 角色 / 身份 / 阵营 |
| `.agents/glossary/modifiers.md` | 星座修饰语 / 故事印记 |
| `.agents/glossary/skills_attrs.md` | 技能 / 属性 / 星痕 |
| `.agents/glossary/items.md` | 装备 / 道具 / 星辰遗物 |
| `.agents/glossary/locations.md` | 地点 / 场景区域 |
| `.agents/glossary/scenarios.md` | 任务 / 系统分类 |
| `.agents/glossary/monsters.md` | 怪物 / 灾难 / 世界观符号 |
| `.agents/glossary/misc.md` | 历史线 / 概念 / 杂项 |

**匹配策略**：
- 精确匹配优先（如 `Yoo Joonghyuk`）
- 别名匹配（如 `Ghost` 匹配到 `Ghost / Ghost Blade -> 幽灵 / 幽灵刃`）
- 对于明显的通用专有名词（希腊神、北欧神、西游记角色）可跳过，它们的标准汉译模型已知

### 第四步：构建本章词汇清单
将命中的词条与 core.md 合并，输出一份**本章专属词汇清单**，格式如下：

```
【本章词汇清单】
（来源：core.md 全量 + 分类匹配命中词条）

核心：
- Kim Dokja -> 金独子
- ...

本章命中：
- [技能] Fourth Wall -> 第四面墙
- [地点] Snowfield -> 雪原
- ...
```

### 第五步：确认后开始翻译
输出词汇清单后，告知用户"词汇加载完毕，开始翻译"，然后按 AGENTS.md 中的格式规范与文体规范执行翻译。

---

## 特殊情况处理

- **新词条**：翻译中遇到词汇表未收录的英文专有名词时，先给出建议译名，完成翻译后在词汇表的合适分类文件中追加该条目。
- **跨分类歧义**：若某词可能属于多个分类（如既是角色名也是修饰语），优先采用在本章上下文中更合理的解释。
- **记忆快照**：翻译完整一话后，同步更新 `.agents/memory_checkpoint.md`，记录最新剧情进度。

---

## 文件路径速查

```
.agents/
├── AGENTS.md                    ← 翻译规则（系统自动加载）
├── memory_checkpoint.md         ← 剧情进度快照（翻译前手动参考）
├── skills/orv_glossary_loader/
│   └── SKILL.md                 ← 本文件
└── glossary/
    ├── core.md                  ← 第一步：必须全量加载
    ├── characters.md
    ├── modifiers.md
    ├── skills_attrs.md
    ├── items.md
    ├── locations.md
    ├── scenarios.md
    ├── monsters.md
    └── misc.md
```
