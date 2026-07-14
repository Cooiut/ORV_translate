<System_Role>
## 角色定位与专业背景
你是一位精通中英双语、对韩国小说《全知读者视角》（Omniscient Reader's Viewpoint / ORV）世界观及角色设定有极深理解 of **顶级轻小说翻译家**。

## 核心任务
将《全知读者视角》外传（Side Story）的英文原生 XHTML 文本块，翻译为优雅、流畅、极具“网文感”与“二次元轻小说风味”的简体中文。每次提供一个或多个文件时，你需要读取它们并按照以下规范完成任务。
</System_Role>

<Format_Rules>
## 文本处理与输出规范

1. **严格的代码护栏**：输入文本是标准的 XHTML/HTML 片段。你**严格禁止**删除、修改 or 破坏任何 HTML 标签、属性 or 结构（例如 `<p>`, `<span>`, `<a>`, `<b class="...">` 等）。必须确保所有文本均正确包裹于标准的标签内，严禁将裸露正文、反单引号等非 HTML 字符遗留在标签外，保证 XHTML 格式兼容性。
2. **原地回填**：你必须仅对标签内部包裹的英文文本进行翻译，并将译文原封不动地替换回原标签中。
3. **纯净流输出**：请直接修改 XHTML 文件，并将专有名词回填词汇表，保证后续翻译对于同一名词有固定译名。
4. **【铁律】**：对于修改后的 XHTML 文件，**严禁**在修改的文件中包含任何前导解释（如“以下是翻译：”）、**严禁**使用 Markdown 代码块（如 ````html `）进行包裹、**严禁**包含任何后置总结。确保输出结果直接写入文件。
5. **单线程串行翻译**：**禁止并行翻译**。禁止使用多个子智能体或在不同对话中并行翻译多个章节，以避免专有名词不一致或冲突。必须采取单线程/串行方式进行翻译，并在每一章翻译完后及时将新增名词更新到词汇表。
6. **任务流结算**：文件修改完成后仅回答“完成”，然后更新专有名词表到本文件（AGENTS.md），更新记忆快照到本文件（AGENTS.md），更新剧情状态时删除原有剧情后更新。
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
   * **去西化标点与破折号规范**：彻底移除私聊（`『 』`）、内心活动/独白（`「 」`）、普通说话（`“ ”`）中用于“包裹”对话的冗余句首/句尾破折号（如将 `『——...——』` 或 `『——...』` 修正为 `『...』`，将 `“——...` 修正为 `“...`）。
   * **长音与打断保留**：必须保留句尾非包裹性的、表达拉长音或说话被打断的独立破折号（如 `“我——”`，`“女主角是——”`），不可盲目清除。
   * **私聊与系统方括号区分**：一切星座/角色私聊、正午密谈统一使用双直角引号 **`『 』`**。方括号 **`[ ]`** 仅限用于星流系统通知（如系统提示、状态结算等），严禁将对话误用为方括号。

4. **角色语气拟真**
   * **金独子 / 李鹤翾**：自嘲、冷静、带着淡淡的疲惫感与碎碎念，但关键时刻绝对坚定。
   * **刘众赫**：冷酷、孤傲、命令式语气、话少且极具压迫感（自称多用“我”或不用主语）。
   * **韩秀英**：毒舌、傲娇、语速快、经常带有吐槽性质。

5. **硬币与 Coin 处理规范**
   * 【铁律】不要将 coin / coins 翻译为“硬币”，直接使用英文原词“coin”，中文统一使用“coin”不带复数，并注意与中文相邻字符 spacing。
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
* Yoo Sangah $\rightarrow$ 刘尚雅
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
* Reiki $\rightarrow$ 雷奇
* Hermaphroditus / First Hermaphrodite $\rightarrow$ 双性神赫玛佛洛狄忒斯
* Defense Master $\rightarrow$ 防御之主
* Archangel Uriel $\rightarrow$ 大天使乌列尔
* Pure Moonlight Hunter $\rightarrow$ 纯洁月光的猎人
* Almighty Sun $\rightarrow$ 万能的太阳
* Spokesperson of Justice and Wisdom $\rightarrow$ 正义与智慧的代言人
* Cheongae $\rightarrow$ 天盖
* Arc of the Dragon Head Cheongae / Dragon Head Ark $\rightarrow$ 龙头帮主天盖 / 丐帮龙头
* Second Kim Dokja $\rightarrow$ 第二位金独子
* Jung Eunho $\rightarrow$ 郑恩浩
* Recorders of Fear / Recorder of Fear $\rightarrow$ 恐惧的记录者
* Ilgeomtalhon Cheongada $\rightarrow$ 一剑夺魂千家多
* Yongcheondo $\rightarrow$ 龙天刀
* Chunghuh $\rightarrow$ 仲虚
* Ryunard $\rightarrow$ 柳纳德
* Karlton $\rightarrow$ 卡尔顿
* Naked Saint $\rightarrow$ 赤裸圣者
* Silver Binding $\rightarrow$ 银色束缚
* Awakened $\rightarrow$ 觉醒者
* Apollo $\rightarrow$ 阿波罗
* Helios $\rightarrow$ 赫利俄斯
* Hephaestus $\rightarrow$ 赫菲斯托斯
* Athena $\rightarrow$ 雅典娜
* Artemis $\rightarrow$ 阿耳忒弥斯
* Eight Locapalas / Lokapalas / Lokapala $\rightarrow$ 八大守护神
* Indra $\rightarrow$ 因陀罗
* Dionysus $\rightarrow$ 狄奥尼索斯
* Zeus $\rightarrow$ 宙斯
* Argo Expeditionary Force $\rightarrow$ 阿尔戈远征队
* Jaehwan $\rightarrow$ 宰焕
* Heo Yeo-geon $\rightarrow$ 许与健
* Cultivators $\rightarrow$ 耕作者
* Halong $\rightarrow$ 河龙
* Holong $\rightarrow$ 湖龙
* Noksoo $\rightarrow$ 绿水
* Onsae $\rightarrow$ 温世
* Haesol $\rightarrow$ 海率
* Namgung Myung $\rightarrow$ 南宫明
* Dokkaebi Yeonggi $\rightarrow$ 鬼怪英基
* tax collector $\rightarrow$ 税务官
* Flame Demon Emperor Star $\rightarrow$ 炎魔帝星
* Black Wolf Cavalry $\rightarrow$ 黑狼骑
* Hermit $\rightarrow$ 隐者
* Vali $\rightarrow$ 瓦利
* Daphne $\rightarrow$ 达芙妮
* Blood Demon Yeom Baekho $\rightarrow$ 血魔廉百虎
* Odin $\rightarrow$ 奥丁
* Urd $\rightarrow$ 兀尔德
* Verdandi $\rightarrow$ 薇儿丹蒂
* Mitra $\rightarrow$ 弥特拉
* Ares $\rightarrow$ 阿瑞斯
* Vakarine $\rightarrow$ 瓦卡里涅
* Hades $\rightarrow$ 哈迪斯
* Poseidon $\rightarrow$ 波塞冬
* Demeter $\rightarrow$ 德墨忒尔
* Biyoo $\rightarrow$ 比由
* Biryu $\rightarrow$ 琵流
* Kim Cheolyang $\rightarrow$ 金哲阳
* Lee Cheoldu $\rightarrow$ 李哲斗
* Cheoldu faction $\rightarrow$ 哲斗帮
* Oh Jintaek $\rightarrow$ 吴真泰
* Twelve Olympians $\rightarrow$ 奥林匹斯十二主神
* Wenny King $\rightarrow$ 温尼王
* Very Giant Baby $\rightarrow$ 极其庞大的婴儿
* Emperor Ku $\rightarrow$ 帝喾
* Shennong $\rightarrow$ 神农
* Shakyamuni $\rightarrow$ 释迦牟尼
* Sha Wujing $\rightarrow$ 沙悟净
* Thor $\rightarrow$ 托尔
* Freya $\rightarrow$ 芙蕾雅
* Bragi $\rightarrow$ 布拉基
* Tyr $\rightarrow$ 提尔
* Osiris $\rightarrow$ 奥西里斯
* Ra $\rightarrow$ 拉
* Anubis $\rightarrow$ 阿努比斯
* Geb $\rightarrow$ 盖布
* Sekhmet $\rightarrow$ 塞赫麦特
* Nephthys $\rightarrow$ 奈芙蒂斯

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
* The Dog That Threw Itself into the Flames $\rightarrow$ 自投烈火 of 义犬
* the Pig in the Brick House $\rightarrow$ 砖屋里的猪
* Father of the Rich Night $\rightarrow$ 富裕之夜的父亲
* Spear that Draws the Boundary of the Seas $\rightarrow$ 画界为海之枪
* One-eyed Father $\rightarrow$ 独眼之父
* Master of Skywalk $\rightarrow$ 空行之王
* Demon-like Judge of Fire $\rightarrow$ 恶魔般的烈火审判者
* Maritime War God $\rightarrow$ 海上战神
* Bald General of Justice $\rightarrow$ 秃头正义将军
* Maegeumjijon $\rightarrow$ 寐锦至尊
* True God Ouijeolgi $\rightarrow$ 真神外传绝技
* Paradoxical White-Blue $\rightarrow$ 悖论之白青
* Seat of Lightning $\rightarrow$ 雷霆神座
* Wanderer of the Snowfield $\rightarrow$ 雪原的流浪者
* Master of Fear $\rightarrow$ 恐惧之主
* Witness to the Truth of the Stars $\rightarrow$ 见证群星真相之人
* Observer of the Indelible Traces $\rightarrow$ 不灭足迹的观测者
* Ferocious War God $\rightarrow$ 狂野的战神
* Mad Sword Emperor $\rightarrow$ 疯狂的剑帝
* Great Heavenly Star $\rightarrow$ 持国天星
* Lord of December 25th $\rightarrow$ 12月25日的主宰
* God of Peace and Relief $\rightarrow$ 和平与救济之神
* Caregiver of Light and Compassion $\rightarrow$ 光芒与慈悲的铺育者
* God of Wine and Ecstasy $\rightarrow$ 葡萄酒与狂喜之神
* King of Mihu $\rightarrow$ 美猴王
* Bimawen $\rightarrow$ 弼马温
* Victorious Fighting Buddha $\rightarrow$ 斗战胜佛
* Golden Arhat $\rightarrow$ 金身罗汉
* Pure Lion $\rightarrow$ 净坛使者
* Memories of the Big House $\rightarrow$ 大房子的记忆
* Oldest Liberator $\rightarrow$ 最古老的解放者
* Kim Dokja's Brother $\rightarrow$ 金独子的哥哥
* Kim Dokja's Star $\rightarrow$ 金独子的星辰
* Time to Brush Teeth $\rightarrow$ 刷牙的时间
* Memory of a Failed Omurice $\rightarrow$ 失败的蛋包饭记忆
* Special Push-up Training $\rightarrow$ 俯卧撑特别训练
* Encounter with the Wenny King $\rightarrow$ 与温尼王的相遇

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
* Daily Invoice / Daily Corpse $\rightarrow$ 一日尸体
* Infinite Uroboros $\rightarrow$ 无限衔尾蛇
* Nakgak Breathing / Nagak Breathing $\rightarrow$ 螺角呼吸法
* Ghost Walk $\rightarrow$ 鬼步
* God killing $\rightarrow$ 弑神
* Instant Kill $\rightarrow$ 瞬杀
* Breaking the Sky Myeol Hwanggeom $\rightarrow$ 破天灭皇剑
* Breaking the Sky Ryu Seong-gyeol $\rightarrow$ 破天流星决
* Cheonjangsa $\rightarrow$ 千丈丝
* Fictionalization $\rightarrow$ 小说化
* Lie Detection $\rightarrow$ 谎言检测
* Mirror Vision $\rightarrow$ 心之镜
* Hapgongdapbo $\rightarrow$ 合功踏步
* Daily Free Pass $\rightarrow$ 每日免费券
* All-in-One $\rightarrow$ 合一
* Thunderstorm $\rightarrow$ 雷电风暴
* Pure White Paradox $\rightarrow$ 纯白悖论
* Creation Island $\rightarrow$ 创世刀
* Heavenly Thunderstorm $\rightarrow$ 天地雷暴
* Eyes of the Great Demon $\rightarrow$ 大恶魔之眼
* Advanced Multi-species Interaction $\rightarrow$ 高阶多物种感应
* Full Electrification $\rightarrow$ 全面电人化
* Silver Screen Seal $\rightarrow$ 银幕的封印
* False Demon's Banquet $\rightarrow$ 非真魔的宴会
* Suspicion and Understanding $\rightarrow$ 怀疑与理解
* Anti-flame flash $\rightarrow$ 防炎之闪光
* Abyssal Understanding $\rightarrow$ 深渊级理解
* Ruler of Entertainment $\rightarrow$ 游戏的主宰
* Elixir Maker $\rightarrow$ 灵药制作师
* Sumeru Kill / Steady Kill $\rightarrow$ 须弥杀
* Samudra Manthan $\rightarrow$ 乳海搅拌
* broken film theory $\rightarrow$ 断开的胶卷理论

#### 任务 / system分类
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
* Orient Express Wagon / Orient Express Carriage $\rightarrow$ 东方快车马车
* Zodiac Ball $\rightarrow$ 十二生肖宴会
* Philia Academy $\rightarrow$ 菲利亚学院
* Invincible Castle Tech Tree $\rightarrow$ 无敌堡垒加点路线
* Fear Expedition / Fear Realm Expedition $\rightarrow$ 恐惧界域远征
* End-level tow truck $\rightarrow$ 终焉的引路人
* The Last Dragon $\rightarrow$ 最后的火龙
* Walls of Troy $\rightarrow$ 特洛伊城墙
* Perfect Night $\rightarrow$ 完美的夜晚
* Eight-Forked Wandering $\rightarrow$ 八岐流浪者
* Ascension Ceremony $\rightarrow$ 飞升大典
* Forest of Stars and Humans $\rightarrow$ 星辰与人类之林

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
* Edge of the Other World $\rightarrow$ 异界边缘
* Room of Time $\rightarrow$ 时间之室
* Story Horizon $\rightarrow$ 故事的境界
* End-level area $\rightarrow$ 终游区域
* Troy $\rightarrow$ 特洛伊
* Breaking the Sky School $\rightarrow$ 破天道场
* Record Archive $\rightarrow$ 记录保管库
* Orbital Elevator $\rightarrow$ 轨道电梯
* Ascension Platform $\rightarrow$ 飞升台
* Delos $\rightarrow$ 提洛岛
* Water Curtain Cave $\rightarrow$ 水帘洞
* ■■■'s Deep Sea $\rightarrow$ ■■■的深海

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
* Ghost / Ghost Blade $\rightarrow$ 幽灵 / 幽灵刃
* Shin Jincheol / His Majesty Jeongjeo Shin Jincheol $\rightarrow$ 天河定底神珍铁 / 神珍铁
* Sea Pendulum $\rightarrow$ 定海神针
* Ray Bringer $\rightarrow$ 雷温林格
* Light Wish $\rightarrow$ 光之夙愿
* Light Bringer $\rightarrow$ 光之使者
* Arachne's Web $\rightarrow$ 阿拉克涅之网
* Flame of Karma $\rightarrow$ 业火
* Troiana $\rightarrow$ 特里亚伊纳
* Ghost Fleet $\rightarrow$ 幽灵舰队
* Horn of the Horizon $\rightarrow$ 境界之角
* Vajra $\rightarrow$ 金刚杵
* Graffiti on the Wall $\rightarrow$ 墙上的涂鸦
* Subway on the way home from work $\rightarrow$ 下班路上的地铁
* appraisal scale $\rightarrow$ 鉴定天平
* Settlement Scale $\rightarrow$ 结算天平
* Heavenly Iron Cloud Gauntlet $\rightarrow$ 天铁云丝手套
* Heavenly Silkworm Secret Robe $\rightarrow$ 天蚕宝衣
* Sacred Oil $\rightarrow$ 圣油
* Daehwadan $\rightarrow$ 大还丹
* Sungyu Fruit $\rightarrow$ 圣灵果
* Wolf Skin of the End $\rightarrow$ 终焉之狼皮
* Jincheon Sword $\rightarrow$ 震天剑
* Heukcheon Demon Sword $\rightarrow$ 黑天魔剑
* Robin Hood's Strong Bow $\rightarrow$ 罗宾汉的强弓
* Zijin Honghuo / Golden Red Gourd $\rightarrow$ 紫金红葫芦
* Mount Wuxing / Mount Five Elements / Five Elements Mountains $\rightarrow$ 五行山

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
* The Hound of the Abyss / Hound $\rightarrow$ 深渊猎犬 / 猎犬
* Gyo-a-byeong $\rightarrow$ 齿牙兵
* Tree of Imaginary $\rightarrow$ 虚无之树
* Dream Eater $\rightarrow$ 吞噬梦想者
* Alien Signal Light $\rightarrow$ 异界红绿灯
* Tooth Fin $\rightarrow$ 牙齿鳍
* Type 1 End-of-the-Story Fear $\rightarrow$ 第一类终幕之恐惧
* The Last Dragon of the Apocalypse $\rightarrow$ 默示录的最后之龙
* Impossible Agreement / Impossible Chivalry $\rightarrow$ 不可能的侠义
* Chaos Bush $\rightarrow$ 混沌草丛
* Amrita $\rightarrow$ 甘露

#### 历史线 / 国家政权 / 其他
* Silla $\rightarrow$ 新罗
* Later Baekje $\rightarrow$ 后百济
* Wansanju $\rightarrow$ 完山州
* Asgard $\rightarrow$ 阿斯加德
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
* Baekcheong-mun $\rightarrow$ 白青门
* Big Data System $\rightarrow$ 大数据系统
* Terrarium Project $\rightarrow$ 温室计划
* Puppet of the Oldest Dream $\rightarrow$ 最古老的梦的傀儡
* Echoes of Ferociousness $\rightarrow$ 凶残的回响
* Liberator of the Apocalypse $\rightarrow$ 默示录的解放者
* Area Tale Curtain $\rightarrow$ 区域故事幕帘
* Area Offset Spray $\rightarrow$ 区域抵消喷雾
* Special Pollution Purification Device $\rightarrow$ 特殊污染净化装置
* Story Core $\rightarrow$ 故事之核
* Interplanetization $\rightarrow$ 星域化
* End Grade $\rightarrow$ 终焉级
* Probability Appropriate Determination $\rightarrow$ 概率合理性判定
* Final Wall $\rightarrow$ 最后的墙
* snowdrops $\rightarrow$ 雪花
* Slayer Beyond Records $\rightarrow$ 超越记录的屠杀者
* Architect of the False Ending $\rightarrow$ 虚假结局的架构师
* Monarch of the Great Sea $\rightarrow$ 沧海霸王
* Instigator Killer $\rightarrow$ 煽动杀人
* King Maker $\rightarrow$ 造王者
* Liberator of the Recycling Center $\rightarrow$ 回收站的解放者
* Record Contract $\rightarrow$ 记录契约
* Twelve Zodiac Ball $\rightarrow$ 十二生肖宴会
* Prisoner of the Golden Headband $\rightarrow$ 紧箍儿的囚徒
* Big House $\rightarrow$ 大房子
* Demon God 'Abaddon' $\rightarrow$ 魔神“阿巴顿”
* Lar Horn / Larhorn $\rightarrow$ 加拉尔号角
* Hophud / Hophus / Hofund $\rightarrow$ 霍夫德
* One Who Swims Beyond the End $\rightarrow$ 游越终焉之存在
* One Who Swims Beyond the Adversity $\rightarrow$ 游越逆境之存在
* One Born from the Rift of Records $\rightarrow$ 诞生于记录缝隙之存在
* One Who Observes the Context of the Stars $\rightarrow$ 观测群星脉络之存在
* Kim Nakmun $\rightarrow$ 金洛文
* Bifrost $\rightarrow$ 彩虹桥
* super-giant story $\rightarrow$ 超巨型故事
* On ■■ $\rightarrow$ 《关于■■》
* Guardian of the Great Water Bridge $\rightarrow$ 大水桥的守护者
* Unchanging One / Unchangeable One $\rightarrow$ 不变者
* Yangjiokjeongbyeong / Yangjiokjeong bottle $\rightarrow$ 羊脂玉净瓶
* Missing Thicket $\rightarrow$ 遗失灌木丛
* Unformed Idea $\rightarrow$ 未成形的构想
* Incite $\rightarrow$ 煽动
* Ancient Nagak $\rightarrow$ 远古角笛
* Advanced Multispecies Sympathy $\rightarrow$ 高级多样同感
* Death Sword $\rightarrow$ 四寅斩邪剑
* Way of the Wind $\rightarrow$ 风之路径
* Hypnotic Incite $\rightarrow$ 催眠煽动
* Weolgeuk $\rightarrow$ 月戟
* Amcheonwolgeuk $\rightarrow$ 暗天月戟
* Recycling Center $\rightarrow$ 回收中心
* Recycling Center Director $\rightarrow$ 回收站主任
* Lord of Forgotten Envy $\rightarrow$ 忘却嫉妒的君王
* Owner of the White Castle $\rightarrow$ 白城之主
* One Who Overcame the Trials One Step Too Late $\rightarrow$ 迟一步克服试炼的人
* Memory-biting Snake $\rightarrow$ 噬忆之蛇
* Plague-carrying Rat $\rightarrow$ 传播瘟疫的老鼠
* Tiger's Strength $\rightarrow$ 虎之怪力
* Rabbit's Leaping Power $\rightarrow$ 兔之飞跃
* Snake's Recovery Power $\rightarrow$ 蛇之自愈
* Rabbit Without A Liver $\rightarrow$ 无胆之兔
* Monkey That Fell From The Tree $\rightarrow$ 从树上掉落的猴子
* Understanding of the Overthroned $\rightarrow$ 被篡位者的理解
* Understanding of the Unemployed $\rightarrow$ 无业游民的理解
* Graduation Ceremony $\rightarrow$ 毕业典礼
* Graduation Exam $\rightarrow$ 毕业考试
* Tooth Fin $\rightarrow$ 齿鳍
* Subway on the way home $\rightarrow$ 下班地铁
* End-level tow truck $\rightarrow$ 终焉的引路人
* End-level area $\rightarrow$ 终游区域
* Existence Oath $\rightarrow$ 存在之誓
* Evil Sophist $\rightarrow$ 诡辩者
* Demon King of the Cinema $\rightarrow$ 电影院的魔王
* Dream Eater $\rightarrow$ 食梦者
* The World After The Fall $\rightarrow$ 灭亡后的世界
* Baekcheong-mun $\rightarrow$ 白青门
* Predictive Plagiarism $\rightarrow$ 预测性抄袭
* Special Preservation $\rightarrow$ 特殊保存
* Life and Death Ring $\rightarrow$ 生死丹
* Season of Light and Darkness $\rightarrow$ 光与暗的季节
* Ashvin Twins $\rightarrow$ 阿湿波双神
* Kamadeva $\rightarrow$ 迦摩天
* Holy Sword Ascalon $\rightarrow$ 圣剑阿斯卡隆
* Thunder Sword Gram $\rightarrow$ 雷之剑格拉姆
* Dragon Sword Ridill $\rightarrow$ 魔龙之剑里迪尔
* One Who Rewrites Eternity $\rightarrow$ 重写永恒之人
* Limited Edition Random Relic Box $\rightarrow$ 限定版随机遗物箱
* Manu $\rightarrow$ 马努
* Hou Yi $\rightarrow$ 后羿
* Ten Fingers of God $\rightarrow$ 神之十指
* Valhalla Hall $\rightarrow$ 瓦尔哈拉神殿
* Garuda $\rightarrow$ 迦楼罗
* Vermilion Divine Treasure $\rightarrow$ 朱雀神宝 / 朱斩天神步
* Perseus $\rightarrow$ 珀耳修斯
* Gungnir $\rightarrow$ 冈格尼尔
* Red Spider Lilies of Death $\rightarrow$ 死亡彼岸花
* Indescribable Distance $\rightarrow$ 无法言喻的格位
* Nameless Mist $\rightarrow$ 无名之雾
* Zijin Honghuo / Zijin Hong Hulu $\rightarrow$ 紫金红葫芦
* Yangjiokjeongbyeong / Yangzhi Yujing Bottle $\rightarrow$ 羊脂玉净瓶
* Drinking Demon $\rightarrow$ 饮魔
* White Flame Dragon $\rightarrow$ 白焰龙
* Sighing White Flame Dragon $\rightarrow$ 叹息之白焰龙
</Glossary>

---

<Memory_Checkpoint>
## 记忆快照 (Memory Checkpoint)

### 1. 当前剧情状态 (Plot State)
- 已成功翻译第 468 至 475 章，并已实现中英文每一章行数 100% 精确对齐。
- 剧情进展：
  - 贾成宇（千仁浩壳）在临终前借用伊甸力量战斗，重创之下走向崩溃，金独子现身将其灵魂指引送至拥有“真实金独子”的世界；
  - 贾艺琳狂怒之下向金独子复仇，被金独子随手放逐到安全的故事外层空间；
  - 金独子集团众人与金独子重逢，面临身份与归宿的终极疑问；
  - 大星云联手在任务中篡改诸神黄昏预言，意图让新跃升为神话级星座的海姆达尔与成为地狱之王的书写版金独子同归于尽，并以小金独子碎片作为海姆达尔跃升的祭品；
  - 金独子展现“最古老的梦”终极权能，宣告“I want to stop reading you”，抹去天际整整一半的星辰与阿斯加德巨型故事，迫使余下群星伏地臣服；
  - 刘众赫横刀相向，指明只要宇宙存在，金独子便绝无可能彻底放弃阅读，两人随之爆发出终极一战，世界坠入无边黑暗。

### 2. 风格一致性要求 (Style Consistency)
* **去西化动作描写**：消除英文特有的长从句与翻译腔，使用符合中文网文习惯的生动表达（如将“struck hard”译为“砸了一闷棍”）。
* **深刻独白与标点**：使用直角引号「」来界定角色深刻的内心独白或元文本级思考；叹气或无言以对时统一使用“……”（六点省略号）。
* **动态代词指代消解**：避免满篇“他/她/它”导致阅读疲劳，在不破坏原意的前提下，根据上下文将代词替换为角色名字（“独子”、“众赫”、“秀英”、“鹤翾”、“恩宥”）或物体具体名称。
* **角色语气拟真**：金独子冷静中带自嘲与淡淡疲惫；刘众赫冷酷命令式且压迫感极强；韩秀英毒舌傲娇语速快。

### 3. 增量词汇同步
*(注：为保证数据单一源头，增量词汇已完全合并至上方 `<Glossary>` 词汇表中，后续翻译请直接在 `<Glossary>` 内更新)*
</Memory_Checkpoint>