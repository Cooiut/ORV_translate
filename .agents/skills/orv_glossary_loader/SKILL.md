---
name: orv_glossary_loader
description: 在开始翻译 ORV 外传章节前触发。扫描待翻译的源文件，从分层词汇表中提取本章相关词条，构建精简词汇上下文，避免全量词汇注入导致的注意力稀释。
---

# ORV 分层词汇加载器

## 触发时机
当用户指示翻译某一章节或某个 XHTML 文件时，**在开始翻译之前**执行以下流程。

---

## 执行步骤

### 第一步：加载核心词汇（必选，无需匹配）
读取 `.agents/glossary/core.md`，将其**全部内容完整纳入**本次翻译的词汇上下文。  
core.md 中的所有词条（含"后期战场高频词"节）无论章节内容如何，均不需要经过匹配判断，直接加载。

### 第二步：双向扫描（先正向再反向）

**正向扫描**——读取源 XHTML 文件，从文本中提取候选词：
- 引号包裹的词组（`'...'`、`"..."`）
- 方括号内的词（`[...]`、`[...]`）
- 连续大写开头的名词短语（≥2个词时识别为整体，如 `Supreme God of Light`）
- 韩文罗马音特征词（含 `oo`, `ae`, `eo`, `hyuk`, `yeon`, `woo`, `eun` 等）

**反向扫描**——对所有分类词汇表中每一条目的英文键名（`->` 左侧），  
逐一检查其是否**出现在源文**中（区分大小写不敏感）。  
反向扫描的优先级高于正向扫描，可捕获正向扫描遗漏的词。

### 第三步：规范化匹配（五步法）

将正向与反向扫描结果合并后，对**未命中的候选词**执行以下规范化处理再次匹配：

```
A. 规范化处理（对候选词和词汇表键名同时执行）：
   - 全部转为小写
   - 去除所有格（'s → 空字符）
   - 连字符与空格统一（super-giant = super giant）
   - 去除首尾引号/括号包裹

B. 双向子串匹配：
   - 词汇表键名 包含 候选词 → 命中
   - 候选词 包含 词汇表键名 → 命中
   （例：源文 "Fear Realm" ⊂ 词汇表 "Fear Realm Expedition" → 命中）

C. 别名展开：
   - 词汇表 "/" 左右的每个英文名均作为独立键名参与匹配
   - 例："Dream Eater / Devourer of Dreams" 中，两个名称各自单独触发

D. 标记未收录词：
   - 若候选词经以上所有步骤仍未命中，不得静默跳过
   - 将其列为 [未收录] 并给出建议译名，供翻译者确认

E. 跳过通用知识词：
   - 仅跳过以下类型：标准神话神名（Zeus、Apollo、Thor 等）、
     标准西游记角色（Monkey King 等）、世界地名（Troy、Olympus 等）
   - 其余一律尝试匹配，匹配失败则进入 D 步骤
```

### 第四步：加载命中词汇表文件

根据第三步命中结果，**按需读取**对应分类文件：

| 分类文件 | 涵盖内容 |
|---|---|
| `.agents/glossary/characters.md` | 角色 / 身份 / 阵营 |
| `.agents/glossary/modifiers.md` | 星座修饰语 / 故事印记 |
| `.agents/glossary/skills_attrs.md` | 技能 / 属性 / 星痕 |
| `.agents/glossary/items.md` | 装备 / 道具 / 星辰遗物 |
| `.agents/glossary/locations.md` | 地点 / 场景区域 |
| `.agents/glossary/scenarios.md` | 任务 / 系统分类 |
| `.agents/glossary/monsters.md` | 怪物 / 灾难 / 世界观符号 |
| `.agents/glossary/misc.md` | 历史线 / 概念 / 杂项 |

若某分类中有任意一个词命中，则读取该文件完整内容（避免部分加载导致遗漏同文件的其他相关词）。

### 第五步：输出本章词汇清单

格式如下，输出后告知用户"词汇加载完毕，开始翻译"：

```
【本章词汇清单】
（来源：core.md 全量 + 分类匹配命中词条）

★ 核心词汇（core.md，略，全量已加载）

★ 本章命中：
  [角色]  Surya -> 苏利亚
  [地点]  Snowfield -> 雪原
  [技能]  Armed Fortress -> 武装堡垒
  ...

⚠ 未收录词（建议译名，请确认）：
  [未收录]  Final Chief Engineer -> 建议译为「最终列车长」
  [未收录]  'Hole' -> 建议译为「深坑」
```

---

## 特殊情况处理

- **新词条确认后追加**：[未收录] 词条经翻译者确认译名后，翻译结束时追加至词汇表对应分类文件末尾（格式：`* 英文原名 -> 中文译名`）。
- **晋升 core.md**：若某词条连续在3章以上出现，翻译结束后将其移入 `core.md` 的"后期战场高频词"节。
- **记忆快照**：翻译完整一话后，同步更新 `.agents/memory_checkpoint.md`。

---

## 文件路径速查

```
.agents/
├── AGENTS.md                    ← 翻译规则（系统自动加载）
├── memory_checkpoint.md         ← 剧情进度快照（翻译前手动参考）
├── skills/orv_glossary_loader/
│   └── SKILL.md                 ← 本文件
└── glossary/
    ├── core.md                  ← 第一步：必须全量加载（含高频词节）
    ├── characters.md
    ├── modifiers.md
    ├── skills_attrs.md
    ├── items.md
    ├── locations.md
    ├── scenarios.md
    ├── monsters.md
    └── misc.md
```
