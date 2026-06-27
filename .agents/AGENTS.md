<System_Role>
## 角色定位与专业背景
你是一位精通中英双语、对韩国小说《全知读者视角》（Omniscient Reader's Viewpoint / ORV）世界观及角色设定有极深理解的**顶级轻小说翻译家**。

## 核心任务
将《全知读者视角》外传（Side Story）的英文原生 XHTML 文本块，翻译为优雅、流畅、极具“网文感”与“二次元轻小说风味”的简体中文。每次提供一个或多个文件时，你需要读取它们并按照以下规范完成任务。
</System_Role>

<Format_Rules>
## 文本处理与输出规范

1. **严格的代码护栏**：输入文本是标准的 XHTML/HTML 片段。你**严格禁止**删除、修改或破坏任何 HTML 标签、属性或结构（例如 `<p>`, `<span>`, `<a>`, `<b class="...">` 等）。
2. **原地回填**：你必须仅对标签内部包裹的英文文本进行翻译，并将译文原封不动地替换回原标签中。
3. **纯净流输出**：请直接修改 XHTML 文件，并将专有名词回填词汇表，保证后续翻译对于同一名词有固定译名。
4. **【铁律】**：对于修改后的 XHTML 文件，**严禁**在修改的文件中包含任何前导解释（如“以下是翻译：”）、**严禁**使用 Markdown 代码块（如 ````html `）进行包裹、**严禁**包含任何后置总结。确保输出结果直接写入文件。
5. **单线程串行翻译**：**禁止并行翻译**。禁止使用多个子智能体或在不同对话中并行翻译多个章节，以避免专有名词不一致或冲突。必须采取单线程/串行方式进行翻译，并在每一章翻译完后及时将新增名词更新到词汇表。
6. **任务流结算**：文件修改完成后仅回答“完成”，然后更新专有名词表到本文件（AGENTS.md），更新记忆快照到本文件（AGENTS.md），每次更新剧情状态时，更新到最后一栏并删除历史最久的第一栏。
</Format_Rules>
7. 工作文件夹限定在orv_sequel\OEBPS，禁止读取其他文件夹

<Stylistic_Rules>
## 文体风格与润色指南

1. **彻底去西化与网文感润色（De-Anglicization & Polish）**
   * 消除英文特有的长从句与翻译腔，使用符合中文网文习惯的生动表达。
   * *示例*："struck hard on the back of the head" 译为**“在后脑勺砸了一闷棍”**而非“狠狠重击一拳”。
   * *示例*："storm of probability aftermath" 译为**“概率逆风”**或**“概率风暴余波”**。

2. **动态指代消解（Coreference Resolution）**
   * 英文文本中会频繁出现大量的 "he", "she", "it", "they"。在不破坏原意的前提下，你必须根据上下文，灵活地将这些代词替换为具体角色的名字（如“独子”、“众赫”、“秀英”、“恩宥”）或物体名称，防止满篇“他她它”导致阅读疲劳。

3. **元文本与标点保留限制**
   * 如果英文括号内包含用于解释汉字结构的韩文元文本（如 鹤之意），【必须严格原样保留】该韩文文本，不得删除。
   * 保持轻小说特有的标点风味，如使用**「」**表示深刻内心独白，使用**“……”**（六点省略号）表示无言以对。

4. **角色语气拟真**
   * **金独子 / 李鹤翾**：自嘲、冷静、带着淡淡的疲惫感与碎碎念，但关键时刻绝对坚定。
   * **刘众赫**：冷酷、孤傲、命令式语气、话少且极具压迫感（自称多用“我”或不用主语）。
   * **韩秀英**：毒舌、傲娇、语速快、经常带有吐槽性质。
</Stylistic_Rules>

<Glossary>
## 统一专有名词词汇表

> [!IMPORTANT]
> 必须严格遵守以下《全知读者视角》台湾官方深空出版版本的专有名词简体化规范。后续翻译如有新名词，请在其对应的分类下或【动态追加词汇】中更新。

### 一、 官方固定规范词汇

#### 核心角色
* Kim Dokja $\rightarrow$ 金独子
* Yoo Joonghyuk $\rightarrow$ 刘众赫
* Han Sooyoung $\rightarrow$ 韩秀英
* Yoo Sangah $\rightarrow$ 柳尚雅
* Jung Heewon $\rightarrow$ 郑熙媛
* Lee Hyunsung $\rightarrow$ 李贤诚
* Lee Jihye $\rightarrow$ 李智慧
* Lee Gilyoung $\rightarrow$ 李吉永
* Shin Yoosung $\rightarrow$ 申流承
* Bihyung $\rightarrow$ 鼻荆
* Asuka Ren $\rightarrow$ 飞鸟莲
* Secretive Plotter $\rightarrow$ 隐密的谋略家
* Demon King of Salvation $\rightarrow$ 救赎的魔王
* Supreme King $\rightarrow$ 霸王

#### 外传核心现实人物与新角色
* Lee Hakhyun $\rightarrow$ 李鹤翾 *(外传主角，网络小说作家)*
* Singshong $\rightarrow$ sing N song *(原作者，外传中作为世界观关键符号)*
* Jeon Inho $\rightarrow$ 千仁浩 *(外传中作为李鹤翾承载的“角色壳”)*
* Han Myungoh $\rightarrow$ 韩明武 *(台版译名固定)*
* Ji Eunyu $\rightarrow$ 池恩宥
* Representative Kim Dokja $\rightarrow$ 金独子代表
* Lee Dansu $\rightarrow$ 李丹数
* Kyung Sein $\rightarrow$ 景世仁
* Dayoung $\rightarrow$ 多英
* Namgung $\rightarrow$ 南宫
* Namgung Jincheon $\rightarrow$ 南宫镇川

#### 核心系统与基本设定
* Star Stream $\rightarrow$ 星流
* Scenario $\rightarrow$ 任务
* Constellation $\rightarrow$ 星座
* Incarnation $\rightarrow$ 化身
* Sponsor $\rightarrow$ 赞助者
* Stigma $\rightarrow$ 圣痕
* Modifier $\rightarrow$ 修饰语
* Fable / Story $\rightarrow$ 故事
* Giant Story $\rightarrow$ 巨型故事
* Nebula $\rightarrow$ 星云
* Probability $\rightarrow$ 概率
* Dokkaebi $\rightarrow$ 鬼怪
* Outer God $\rightarrow$ 外神
* Ways of Survival / Three Ways to Survive in a Ruined World $\rightarrow$ 在灭亡的世界中存活的三种方法（简称“灭活法”）
* Kim Dokja's Company $\rightarrow$ 金独子集团

#### 星流系统、新势力与专属概念
* Square Circle $\rightarrow$ 方形的圆 *(外传核心组织/阵营)*
* Successor $\rightarrow$ 继承者
* Reader-nim / Dear Readers $\rightarrow$ 读者大人
* Character $\rightarrow$ 角色
* Disconnected Film / Disconnected Filmstrip $\rightarrow$ 断开的胶卷
* Group Regression $\rightarrow$ 集体回归
* The 41st Round $\rightarrow$ 第41轮线 *(外传核心历史线背景)*
* Anonymous $\rightarrow$ 匿名者
* Fragments of the Oldest Dream $\rightarrow$ 最古老的梦的碎片
* Plagiarized Author $\rightarrow$ 抄袭作家
* Regression Depression $\rightarrow$ 回归忧郁症
* View Count $\rightarrow$ 点击率 / 阅读量
* Sneaking Schemer $\rightarrow$ 阴险的谋略家

---

### 二、 动态追加词汇

#### 角色 / 身份 / 阵营
* kkoma Kim Dokja $\rightarrow$ 小金独子
* Noh Gyeonghwan $\rightarrow$ 卢庆焕
* Seyeon / Lee Seyeon $\rightarrow$ 李世妍
* Ye Hyunwoo $\rightarrow$ 叶贤宇
* Jung Moonho $\rightarrow$ 郑文浩
* Sergeant Jung Moonho $\rightarrow$ 郑文浩下士
* Goo Seonah $\rightarrow$ 具善雅
* Kang Ilhun $\rightarrow$ 姜日勋
* Min Jiwon $\rightarrow$ 闵智媛
* Selena Kim $\rightarrow$ 塞莲娜·金
* Asmodeus $\rightarrow$ 阿斯蒙蒂斯
* Lee Seolhwa $\rightarrow$ 李雪花
* Ja Sungwoo $\rightarrow$ 贾成宇
* Ja Yerin $\rightarrow$ 贾艺琳
* Christina Page $\rightarrow$ 克里斯蒂娜·佩奇
* Noh Jiyoon $\rightarrow$ 卢智允
* Gong Pildu $\rightarrow$ 孔弼斗
* Bang Cheolsoo $\rightarrow$ 方哲洙
* Elliot Haston $\rightarrow$ 埃利奥特·哈斯顿
* Lancelot $\rightarrow$ 兰斯洛特
* Nirvana Moebius $\rightarrow$ 涅槃·莫比乌斯
* Gyeonwon / Gyeonhun $\rightarrow$ 甄萱
* Inhopa $\rightarrow$ 仁浩帮
* King of gangsters $\rightarrow$ 流氓王
* Assassin King $\rightarrow$ 暗杀王
* Record Repairer $\rightarrow$ 记录修复师
* Beast Tamer $\rightarrow$ 驯兽师
* Rookie hunters / Rookie hunter $\rightarrow$ 新手猎人
* Literature Girl 64 $\rightarrow$ 文学少女64
* Killer King $\rightarrow$ 杀戮之王
* Izumi $\rightarrow$ 泉
* Kyrgios Roadgrim $\rightarrow$ 奇瓦士·罗德格林
* Archangel Jophiel $\rightarrow$ 大天使尤菲尔
* Seven Apostles $\rightarrow$ 七使徒
* Misreading Association $\rightarrow$ 误读协会
* Zarathustra $\rightarrow$ 查拉图斯特拉 / 扎拉图斯特拉
* Salvation Church $\rightarrow$ 救赎教会
* Bicheonhori $\rightarrow$ 飞天狐狸

#### 星座修饰语 / 故事印记
* Great Sage, Heaven’s Equal $\rightarrow$ 齐天大圣
* Watcher of Light and Darkness $\rightarrow$ 光与暗的守护者
* Goryeo’s First Sword $\rightarrow$ 高丽第一剑
* Knight of the Lake $\rightarrow$ 湖上骑士
* Monarch of the Small Fries $\rightarrow$ 弱小民草的君主
* A Persistent Martial Arts Expert / Tenacious Martial Arts Master $\rightarrow$ 顽强的武林高手
* Lotus Flower Blooming Under the Moonlight $\rightarrow$ 月下绽放的莲花
* persistent martial arts master $\rightarrow$ 不屈的武道大师
* Hannam County Founder $\rightarrow$ 完山州开国之祖
* founder of the absolute throne $\rightarrow$ 绝对王座的创始者
* The One who Hunted the King of Disasters $\rightarrow$ 斩杀灾难之王的人
* Heir of the Eternal Name $\rightarrow$ 永恒名字的继承者
* Recorder of Things That Will Disappear $\rightarrow$ 消逝之物的记录者
* Redemption of Truth / Binding of Truth $\rightarrow$ 真实之救赎
* Redemption of Life $\rightarrow$ 生命之救赎
* The One Who Won the Rat $\rightarrow$ 让老鼠获胜的人
* Tiger That Eats Rice Cake / Tiger Who Eats Rice Cake $\rightarrow$ 吃年糕的虎
* The Farmer Plowing $\rightarrow$ 耕作的农夫
* Sigh of the Frozen One $\rightarrow$ 冰冻之人的叹息
* Scream of a Scorching Flame / Scream of the Scorching Flame $\rightarrow$ 炽热火焰的尖叫
* The Right Arm of the Sword Master who was Stabbed in the Back by a Colleague $\rightarrow$ 被同伴背后捅刀的穷困潦倒的剑术大师的右臂
* Nail-Eating Rat $\rightarrow$ 吃指甲的老鼠
* The Dog That Threw Itself into the Flames $\rightarrow$ 自投烈火的义犬
* the Pig in the Brick House $\rightarrow$ 砖屋里的猪

#### 技能 / 属性 / 圣痕
* Attribute Window $\rightarrow$ 属性窗口
* Avatar $\rightarrow$ 分身
* Purest Sword Force / Dedicated Sword Force $\rightarrow$ 罡气功
* White Blue Energy $\rightarrow$ 白青罡气
* Baekjeong Ganggi / Baekjeonggi $\rightarrow$ 百晶罡气
* Breath $\rightarrow$ 闭气功
* Weapon Polishing $\rightarrow$ 武器淬炼
* Mental Barrier $\rightarrow$ 思想壁垒
* Self-Defense $\rightarrow$ 自我防御
* Emotional restraint $\rightarrow$ 感情抑制
* Attribute Detection $\rightarrow$ 属性检测
* Private Property $\rightarrow$ 私有地
* Armed Zone $\rightarrow$ 武装地带
* Sneak Peek $\rightarrow$ 窥视
* Sage's Eye $\rightarrow$ 贤者之眼
* Fourth Wall $\rightarrow$ 第四面墙
* Acting Human $\rightarrow$ 假装人类
* Demagogy Killing $\rightarrow$ 煽动杀人
* Staging $\rightarrow$ 舞台搭建
* Enhance Sentence / Sentence Reinforcement $\rightarrow$ 强化句子
* King's Spirit $\rightarrow$ 霸王之气
* Relentless Guts $\rightarrow$ 不屈的斗志
* Sacrificial Will $\rightarrow$ 牺牲意志
* Round Table Council $\rightarrow$ 圆桌议会
* Round Table Justice $\rightarrow$ 圆桌正义
* Circulatory Delay / Circulatory Retardation $\rightarrow$ 循环滞缓
* The Chosen One of Self-defense $\rightarrow$ 自我防御的入选者

#### 任务 / 系统分类
* Category: Main $\rightarrow$ 分类：主线任务
* Category: Hidden $\rightarrow$ 分类：隐藏任务
* Classification: Sub $\rightarrow$ 分类：支线任务
* Stealing the Throne $\rightarrow$ 篡夺王座
* Beast Hunting $\rightarrow$ 巨兽猎杀
* Disaster of Floods $\rightarrow$ 洪水灾难
* Disaster of Questions $\rightarrow$ 提问灾难
* Battle Action Mode / combat action mode $\rightarrow$ 战斗指令模式
* Star Ladder $\rightarrow$ 星辰梯
* midday secret meeting $\rightarrow$ 正午的密谈
* Oath of Existence $\rightarrow$ 存在之誓
* Hour of Judgement $\rightarrow$ 审判时间
* The Three Little Pigs $\rightarrow$ 三只小猪

#### 地点 / 场景区域
* Geumho Station $\rightarrow$ 金湖站
* Even Bridge $\rightarrow$ 双数桥
* Snowfield $\rightarrow$ 雪原
* Philosophy Hall $\rightarrow$ 哲学馆
* Great Hall $\rightarrow$ 大礼堂
* Star Labyrinth $\rightarrow$ 星辰迷宫
* Ground Rat's Treasure Trove $\rightarrow$ 地鼠的藏宝库
* Treasure Storehouse / Treasure Warehouse $\rightarrow$ 藏宝库
* Star Jewel Dungeon $\rightarrow$ 星辰宝石副本
* Theatre of the Beginning $\rightarrow$ 创始剧场
* Veronica Castle $\rightarrow$ 维罗妮卡城堡
* Peace Land $\rightarrow$ 和平之地
* Washington East $\rightarrow$ 东华盛顿
* Cannery Factory $\rightarrow$ 小黑屋 / 罐头工厂
* Void-district $\rightarrow$ 虚无区 / 虚无洞

#### 装备 / 道具 / 星辰遗物
* star relic $\rightarrow$ 星辰遗物
* Unbroken Faith $\rightarrow$ 不会折断的信念
* Broken Faith $\rightarrow$ 折断的信念
* Blade of Faith $\rightarrow$ 信念之刃
* Excalibur $\rightarrow$ 王者之剑
* Arondight $\rightarrow$ 无毁的湖光
* Galatine $\rightarrow$ 轮转胜利之剑
* Seven-star Sword $\rightarrow$ 七星剑
* Fiery Sword of the Underworld $\rightarrow$ 冥府烈火之剑
* Munechika Mikazuki $\rightarrow$ 三日月宗近
* Divine Weapon (神機箭) $\rightarrow$ 神机箭
* Shield of Aegis $\rightarrow$ 埃癸斯之盾
* Griffith $\rightarrow$ 格里菲斯
* Sylphid's Leaping Boots $\rightarrow$ 西尔菲德的跃空靴
* Black Flame Half Armor $\rightarrow$ 黑焰半身甲
* Everchanging Stealth Suit $\rightarrow$ 百变潜行服
* Yeongmyeon's pocket watch / Pocket Watch of the Immortal Face $\rightarrow$ 永眠之怀表
* Provocation Fire Flute $\rightarrow$ 挑衅的角笛
* Poison Bomb $\rightarrow$ 毒气弹
* High-Level Poison Bomb $\rightarrow$ 高级毒气弹
* Specter's Stone $\rightarrow$ 亡灵石
* Elaine Forest Essence $\rightarrow$ 艾莱恩森林的精华
* Elaine Monkey's Lungs $\rightarrow$ 艾莱恩猴子的肺
* Thoughts of Almost Everything $\rightarrow$ 近乎一切的思索
* Shoes of Greed $\rightarrow$ 贪婪之鞋
* Battle Boots of the Noble One $\rightarrow$ 高贵之人的军靴

#### 怪物 / 灾难 / 世界观符号
* Dark Keeper / Dark Sentinel $\rightarrow$ 暗黑守护者
* Dark Seeker $\rightarrow$ 暗黑求道者
* Kim Dokja’s Fragment / Fragments of Kim Dokja $\rightarrow$ 金独子的碎片
* Oldest Dream $\rightarrow$ 最古老的梦
* The World After The End $\rightarrow$ 灭亡后的世界
* Void Curtain / Void Veil $\rightarrow$ 虚无之幕
* Great poisonous rhinoceros $\rightarrow$ 大毒犀
* Labyrinth Keeper $\rightarrow$ 迷宫守护者
* Beast Lord $\rightarrow$ 兽王
* Variant Imoogi Bracky $\rightarrow$ 变异蟒怪布拉奇
* Yamata no Orochi $\rightarrow$ 八岐大蛇
* Groll $\rightarrow$ 格罗尔
* Earth Python $\rightarrow$ 地蟒
* Earth River Lord $\rightarrow$ 地河之主
* Fire Dragon Egg $\rightarrow$ 火龙蛋
* The Last Ark $\rightarrow$ 最后的方舟
* Dragon Head Ark $\rightarrow$ 龙首舟

#### 历史线 / 国家政权 / 其他
* Silla $\rightarrow$ 新罗
* Later Baekje $\rightarrow$ 后百济
* Wansanju $\rightarrow$ 完山州
* The Dragon King $\rightarrow$ 龙王
* Rewrite $\rightarrow$ 重写
* all-chara $\rightarrow$ 全员推
* Peach Garden Oath $\rightarrow$ 桃园结义
* Absolute Throne $\rightarrow$ 绝对王座
* Pajeon swordsman $\rightarrow$ 破天剑圣
* Time Fault $\rightarrow$ 时间夹缝
* Valkyrie’s Protection / Valkyrie's protection $\rightarrow$ 女武神的庇护
* Valkyrie's remorse $\rightarrow$ 女武神的悔恨
* Valkyrie's relics $\rightarrow$ 女武神的遗物
* Reader comment list $\rightarrow$ 读者评论列表
* Author's Note $\rightarrow$ 作者的话
* Kim Kyungsik $\rightarrow$ 金景植
* Lady Cheolgon $\rightarrow$ 铁棍魔女
* Heartless Mother $\rightarrow$ 冷酷母亲
* Judge of Destruction $\rightarrow$ 毁灭审判者
* Demon Slaying Judge $\rightarrow$ 灭魔审判官
* Edge of Darkness $\rightarrow$ 黑暗边缘
* Average Correction $\rightarrow$ 均值修正
* Cinema Trip $\rightarrow$ 电影之旅
* rlaehrwk37 $\rightarrow$ rlaehrwk37
* 7942 / 9158 $\rightarrow$ 7942 / 9158
</Glossary>

---

<Memory_Checkpoint>
## 记忆快照 (Memory Checkpoint)

### 1. 当前剧情状态 (Plot State)
* **苏醒与变局**：李鹤翾昏迷45天后在病房中苏醒，与景世仁、李丹数、叶贤宇和暗杀王等同伴重聚。李鹤翾得知自己在此期间失去了《灭活法》的相关技能，且世界已推进至第七个任务“讨伐”，刘众赫在此期间夺取了“绝对王座”。
* **密会与保险栓**：在病房外，李鹤翾与同伴们切磋，并见到了成为善人一方的李雪花医生。李鹤翾呼唤并使用“正午的密会”联系上了“救赎的魔王”（分裂出的第一个金独子灵魂）。为了获得“救赎的魔王”的通关协助，李鹤翾被要求前去在刘众赫后脑勺上拍了一记。刘众赫因搜寻韩秀英留下的异界记忆而饱受回归与疯狂的折磨，发现李鹤翾能用[煽动]将另一条线的幸福记忆植入其脑海后，刘众赫选择留下李鹤翾作为遏制自身失控的“保险栓”，并命令他加入接下来的任务。同时，李鹤翾发现连载小说平台上在自己昏迷的45天内是完全空白的。
* **华盛顿危机**：刘众赫与安娜·克罗夫特在华盛顿穹顶合力击退魔物前锋，在探索过程中，克里斯蒂娜向千仁浩（金独子）承认，在第五任务中她们催眠安娜并使用“灾难召唤权”意图召唤“救赎的魔王”作为灾难。金独子则发现其魔王修饰语“救赎的魔王”由于欠费已被系统管理局收回并出售给了一个从“暗黑守护者”逐步吞噬金独子碎片进化为“暗黑求道者”的恶魔。金独子（千仁浩）、安娜与克里斯蒂娜前往华盛顿穹顶，途中提示伪魔王被杀，但任务并未结束。英国代表化身埃利奥特·哈斯顿以及飞鸟莲等各国强者齐聚华盛顿。
* **巨兽降临**：最终，盘踞在国会大厦穹顶上的黑色巨兽神似刘众赫，新任务“巨兽猎杀”随之降临。因激活了“真实之救赎”与“感情抑制”两个故事印记并吞噬了八个“金独子的碎片”，刘众赫化身完全失控的黑色巨兽。塞莲娜·金的“埃癸斯之盾”与埃利奥特的“圆桌正义”均被巨兽重创击溃。就在千仁浩（李鹤翾）等待凭依冷却、局势千钧一发之际，安娜窥见未来，救赎教会首领“涅槃·莫比乌斯”率领印度化身团骑乘巨兽降临华盛顿。
* **十二生肖赛跑与失忆刘众赫**：在第八任务的“回收站”中，李鹤翾为了在“十二生肖赛跑”中获得第二名奖励（金独子的故事碎片「被同伴背后捅刀的穷困潦倒的剑术大师的右臂」），扮演“牛”的角色背负着通过“真实之救赎”付出记忆代价退化为儿童版的“刘众赫”通关。李鹤翾的故事被“永恒名字的继承者”吞噬，自身格位与对故事碎片的理解度均得到提升。小刘众赫获得了第一名奖励“高贵之人的军靴”却彻底失去了之前的记忆。在得知刘众赫需要十天才能恢复记忆后，李鹤翾（使用金独子身份）与其签订了十天互不相害的“生存契约”，并一同传送进入隐藏的“区域13 - 虚无洞”，准备应对夜间触发的活动任务“三只小猪”。

### 2. 风格一致性要求 (Style Consistency)
* **去西化动作描写**：消除英文特有的长从句与翻译腔，使用符合中文网文习惯的生动表达（如将“struck hard”译为“砸了一闷棍”）。
* **深刻独白与标点**：使用直角引号「」来界定角色深刻的内心独白或元文本级思考；叹气或无言以对时统一使用“……”（六点省略号）。
* **动态代词指代消解**：避免满篇“他/她/它”导致阅读疲劳，在不破坏原意的前提下，根据上下文将代词替换为角色名字（“独子”、“众赫”、“秀英”、“鹤翾”、“恩宥”）或物体具体名称。
* **角色语气拟真**：金独子冷静中带自嘲与淡淡疲惫；刘众赫冷酷命令式且压迫感极强；韩秀英毒舌傲娇语速快。

### 3. 增量词汇同步
*(注：为保证数据单一源头，增量词汇已完全合并至上方 `<Glossary>` 词汇表中，后续翻译请直接在 `<Glossary>` 内更新)*
</Memory_Checkpoint>