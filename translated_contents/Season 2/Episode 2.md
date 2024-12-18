# 你好，世界

每一种新编程语言的诞生，都是为了实现之前不可能做到的事情。如今，有很多选择。但你真的需要了解哪些呢？

这一集深入探讨编程语言的历史。我们要致敬“惊人的格蕾丝”，也就是格蕾丝·霍普海军少将。正是由于她的贡献，开发者们无需拥有数学博士学位，就能用机器代码编写程序。我们邀请了来自Jupyter项目的Carol Willing，她曾担任Python软件基金会的主任，以及《纽约时报杂志》和《连线》杂志的撰稿人Clive Thompson，他正在撰写一本关于程序员思维的书。

## 00:07-Multiple voices

你好，世界。

## 00:12-Saron Yitbarek

你好，世界。这是信号，还是噪音？我们作为开发者所做的所有工作，所有无数的编码、压力和测试，最终都归结为一个问题：我们的信号是否传达出来了？

## 00:29-Multiple voices

你好。

## 00:29-Saron Yitbarek

还是说我们的信号丢失了？我们只是在制造噪音。

## 00:40-Saron Yitbarek

我是Saron Yitbarek，这里是《Command Line Heroes》第二季，Red Hat原创播客。在今天的节目中，我们要讨论编程语言：它们的起源，以及我们如何选择学习哪些语言。我们将深入探讨我们与机器沟通的方式。这些语言是如何演变的，以及我们如何利用它们让工作更出色。

## 01:08-Siri

黛西，黛西，告诉我你真实的答案。

## 01:11-Saron Yitbarek

如果你像我一样是个开发者，你可能感受到要成为多语言开发者的压力，流利掌握多种语言。你得懂Java，Python，JavaScript，Node。还得能用C++做梦。也许还得了解像COBOL这样的经典语言，以便增加你的可信度。甚至可能还会担心像Dart这样的新语言……真让人筋疲力尽。

## 01:36-Saron Yitbarek

奇怪的是，我们谈论的电脑其实只会一种语言：机器语言。那些飞速流动的零和一，所有的比特。我们学习的每一种语言，最终都是通往同一个地方的另一条路径。不管我们在工作中有多抽象，最终都会被简化。

## 02:03-Saron Yitbarek

我希望你在故事开始时记住这一点，因为我们要从一个完全辉煌的时刻开始，那个时刻是有一位女性说：“你知道吗？我是一名人类。我不说比特，我也不以比特思考。我想用英语单词编程。”

## 02:22-Saron Yitbarek

今天看来似乎是个简单的概念，但曾几何时，这个想法——人们应该能够用自己的方式与计算机交流——在最佳情况下是个笑话，在最坏的情况下则是亵渎。

## 02:37-Saron Yitbarek

《Command Line Heroes》第二季将围绕支撑我们所做一切的基础展开。这集的英雄是一位女性，她的经历是你想要全面理解现实所需了解的。因此，我向你介绍：软件的第一夫人。

## 02:58-Speaker 5

各位女士们，先生们，我很高兴地向大家介绍格蕾丝·霍普海军准将。谢谢。

## 03:02-Grace Hopper

我去加拿大在圭尔夫大学演讲，得通过多伦多机场的移民局。我把护照递给移民官，他看了看我的护照，又看了看我，然后问：“你是什么？”

## 03:17-Grace Hopper

我说：“美国海军。”

## 03:20-Grace Hopper

他又仔细看了我一眼，然后说：“你一定是他们最年长的。”

## 03:28-Saron Yitbarek

那是1985年的格蕾丝·霍普海军准将。当时她79岁，正在麻省理工学院发表她著名的演讲。即便那时，格蕾丝·霍普已经是一位传奇。她是独立编程语言的教母，使用编译器让我们能够使用人类语言，而不是数学符号。

## 03:51-Saron Yitbarek

她获得了国家技术奖章，去世后又获得了国家自由奖章。所以：她可不是个无名小卒。人们称她为“了不起的格蕾丝”。

## 04:03-Claire Evans

如果说谁注定要成为计算机程序员，那就是格蕾丝。

## 04:06-Saron Yitbarek

这是克莱尔·埃文斯，她是一位科技记者，也是《宽带》一书的作者，书中讲述了科技领域的先锋女性。埃文斯描述了格蕾丝·霍普在1940年代踏入的早期计算机世界，那时她还是一名年轻的海军预备役军人，而计算机的体积相当于一个小房间。

## 04:25-Claire Evans

那些早期的程序员就像一个神职人员。他们是那些在极其繁琐的工作中特别出色的人，因为那是在没有编译器和编程语言的时代，人们真的在机器层面逐位编程。

## 04:42-Claire Evans

要有勇气做那种事情，你真的必须是特定类型的人，而格蕾丝就是那种人。

## 04:49-Saron Yitbarek

她立刻意识到，让人类使用为机器设计的语言是多么限制。这就像试图通过告诉你身体里的每个原子该做什么来走在街上。可能吗？当然可以。有效吗？不。

## 05:06-Saron Yitbarek

程序员的意图与计算机的行为之间必须有一个捷径。自从算盘出现以来，人类就一直在机械化数学思维。显然，有必要再次为计算机找到一种方法。

## 05:19-Claire Evans

在过去，数学家们必须进行所有这些算术。所有这些繁琐的逐步工作，以便找到真正有趣的解决方案。然后计算机的出现提供了通过机器进行算术运算的可能性，从而解放数学家去思考高深、系统化的思想。

## 05:39-Claire Evans

然而，事情并没有如此发展。最终，计算机的出现让数学家不得不成为程序员，他们又一次被困在那些逐位的、繁琐的规则导向的小计算中，以便编写程序。

## 05:53-Claire Evans

所以，我认为格蕾丝的观点是，她希望确保计算机能够帮助数学家思考伟大的思想，做伟大的事情，而不被细节所拖累。

## 06:12-Saron Yitbarek

霍普加入了一条悠久的思想者的队伍。你可以追溯到17世纪的帕斯卡尔，发明了第一台计算器；19世纪的巴贝奇，提出了分析机。那些希望构建工具来增强人类思维的发明家们形成了一条美丽的脉络。正是这条脉络让格蕾丝·霍普在发明被认为不可能的东西时感到自信。

## 06:42-Claire Evans

我意思是，格蕾丝认为人们应该能够用自然语言与计算机进行交流，而这种语言应该是与机器无关的，因此在不同的计算机器之间具有互操作性，这在当时是革命性的想法。

## 06:59-Claire Evans

支持她这一理念的人，最初称之为“自动编程”的想法，在程序员和计算机社区中被视为异类。

## 07:12-Claire Evans

而那些不支持的人最终被称为“尼安德特人”，这在计算机社区中造成了巨大的裂痕。

## 07:21-Saron Yitbarek

霍普并没有轻松说服她的上级跨越那道鸿沟。但她视这是她的责任，决心去尝试。

## 07:30-Grace Hopper

这里总有一条界限。那条线代表了你老板在那一时刻的信念。当然，如果你跨越了它，你就得不到预算。所以你对那条线有双重责任：不要跨越它，同时也要不断教育你的老板，以便把界线推得更远，这样下次你就能更进一步。

## 07:52-Saron Yitbarek

她所推动的未来就是我们的现在。几乎每一种我们依赖的语言都欠霍普和她的第一个编译器一个人情。所以，这场较量是“太空飞行员”胜利，“尼安德特人”失败。

## 08:07-Saron Yitbarek

我们可以用人类语言而不是数字来编码的想法，突然之间你可以输入“转到操作8”或者“关闭文件C”。这让编程变得更人性化。

## 08:21-Claire Evans

格蕾丝清楚地意识到，计算将改变世界，但如果没有人理解如何访问或使用它，它就不会成为一个改变世界的事物。她希望确保这项技术对尽可能多的人开放，尽可能易于接触。

## 08:37-Claire Evans

这就需要对可理解性和可读性做出一定程度的让步。因此，创造编程语言的愿望最终来自于希望为机器提供更多的入口，而不再是这个“教士”的特权，从而向更广泛的公众和新一代开放。

## 08:59-Saron Yitbarek

我想在这里暂停一下，强调克莱尔所说的：我们今天所知的编程语言源于开放技术的愿望。它希望把技术从数学博士的“教士”手中夺走，让开发变得更加易接近。

## 09:14-Saron Yitbarek

编译器所做的所有工作，背后的动机是同理心和理解。

## 09:21-Saron Yitbarek

克莱尔有一个理论，认为霍普是促成这一变革的女性，这与她在第二次世界大战期间的工作有关。

## 09:29-Claire Evans

她正在解决扫雷问题、弹道学问题、海洋学问题。她将这些不同的学科，代表着战争的暴力、混乱和复杂的现实，转化为在马克一号计算机上运行的程序。

## 09:45-Claire Evans

她知道如何进行语言之间的翻译。我所说的并不是计算机语言，而是人类语言。她理解如何倾听那些提出复杂问题的人，试图了解他们的背景、约束和他们学科的特性，然后将其翻译成计算机能够理解的东西。

## 10:06-Claire Evans

在某种程度上，她就像最早的编译器。她是一个具有人类情感的编译器，因为她明白必须以他人的水平进行沟通。

## 10:17-Saron Yitbarek

编译是一种同情与理解的行为。当我们学习新语言，或想知道为什么某些东西根本不编译时，我想我们都可以记住这一点。编译器的工作应该是与我们的语言和谐共处。

## 10:32-Saron Yitbarek

Grace Hopper 明白，一旦人类能够学会说编程语言，一旦编译器开始将我们的意图翻译成机器语言，那么就像打开了洪水闸门。

## 10:43-Claire Evans

她知道，如果计算机行业无法打破壁垒、变得更开放和广泛发展，那么它永远不会作为一种世界改变的力量发展。而且那些从业者无法与需要将问题“放到机器上”的人进行交流。

## 11:00-Claire Evans

所以，她在这种人类翻译方面非常擅长，这使得她特别适合思考和创造编程语言。

## 11:15-Saron Yitbarek

Hopper 开发的英文风格数据处理语言最终演变成了 COBOL，这很完美，因为 COBOL 不张扬，非常务实，Grace Hopper 也是如此。

## 11:28-Saron Yitbarek

在某种程度上，她给我们提供了一种听起来与她非常相似的语言。像 Hopper 一样，COBOL 也具有持久性，60 年后仍然存在。

## 11:50-Saron Yitbarek

好吧，Grace Hopper 的编译器就像是翻译机，将程序员与他们的机器之间的意义进行翻译。而且它们正在从越来越高的抽象层次进行转换。

## 12:03-Saron Yitbarek

然后，几十年后，我们又加入了语言混合的另一个关键成分。想象一下：自由软件社区在 1980 年代蓬勃发展，但当 Unix 替代品 GNU 创建时，没有任何免费的开源编译器可以配合使用。

## 12:22-Saron Yitbarek

为了让 GNU 为我们提供真正的 Unix 开源替代品，为了让编程语言在开源世界中繁荣，社区需要采取 Grace Hopper 的做法——我们需要一个开源编译器。

## 12:38-Saron Yitbarek

以下是 Red Hat 的平台架构师 Langdon White 讲述当时的情况。

## 12:45-Langdon White

在 80 年代，你仍然可以轻松花一万块钱买一个编译器。免费的部分是个大问题。我可没有多余的一万块来买编译器。此外，我还得为每个目标平台买一个编译器。在那个时候，大多数是 Unix，但有各种不同的版本。

## 13:06-Langdon White

所以你不能只买一个，还得为不同的架构或不同的供应商买多个。

## 13:14-Saron Yitbarek

Langdon 指出，问题不仅仅在于成本。在某些情况下，这关乎编码工作的本身。

## 13:21-Langdon White

人们没有意识到，代码结构的具体方式是有影响的。因此，做嵌套的 for 循环或嵌套的 while 循环在不同的编译器下可能是可以的。

## 13:38-Langdon White

所以，如果你不知道编译器如何优化你的代码，那么很难知道如何编写代码以获得最佳优化。

## 13:49-Saron Yitbarek

可以说，我们需要一个免费的选项，一个可访问的选项，一个值得信赖的选项。我们需要的是 GNU C 编译器，GCC。它于 1987 年首次发布，将 Grace Hopper 的编译器革命与自由软件运动结合起来。

## 14:12-Saron Yitbarek

它标准化了事物，让每个人都可以编译其他人编写的代码。我们语言的丰富性正是得益于那一刻。

## 14:22-Carol Willing

GCC 是开放的，这使得语言提升到了一个不同的水平。

## 14:29-Saron Yitbarek

Carol Willing 在 Project Jupyter 工作，她是 Python 软件基金会的前任主任。

## 14:35-Carol Willing

人们开始意识到，尽管专有语言在当时发挥了作用，但它们不会获得开发者社区的接受和喜爱。因为如果我是开发者，我会想要学习最常用的和最前沿的东西。

## 14:59-Carol Willing

我并不一定想培养一种将我锁定在某一项技术上的技能。我认为 Python 成功的原因之一是它是开源的，语法非常简洁。

## 15:11-Carol Willing

它所做的就是以一种共同的方式快速高效地解决问题，并且允许人们合作。我认为这些都是好的程序和良好库的标志：如果你能以最小的麻烦完成工作，并且可以与他人分享，那就是黄金。

## 15:35-Saron Yitbarek

多年来，GCC 逐渐演变，支持 Java、C++、Ada、Fortran 等等。

## 15:43-Carol Willing

通过拥有像 GCC 这样的共同底层接口，它让人们能够将语言进行定制以满足他们的特定需求。例如，在 Python 世界中，有许多不同的库，尤其是在科学 Python 世界中，我们有 numpy、scikit-image、scikit-learn 等等。

## 16:08-Carol Willing

每个库都有一个更具体的任务，它们以此而闻名。因此，我们还看到生物信息学和自然语言处理等领域。因此，人们能够在一个共同的基础上做许多不同的事情，同时在他们的语言或库中加入元素，帮助他们在特定行业或领域中优化问题解决。

## 16:42-Saron Yitbarek

所以，这就是当编译器技术与开源运动迎头相撞时所发生的事情，对吧？随着时间的推移，这种碰撞创造了一个新社区支持的语言的“大爆炸”，任何人都可以学习和构建。

## 16:58-Saron Yitbarek

今天，有成百上千种编程语言在被使用。

## 17:03-Carol Willing

随着开源的流行和接受度的提高，我们看到语言的激增。现在有一些与手机技术和移动相关的语言，还有帮助游戏开发的不同语言。像 Python 和 Ruby 这样的通用语言，为网络开发和网站、网络应用的交付奠定了基础。

## 17:34-Saron Yitbarek

这个列表还在继续。是的，我们正在构建的巴别塔在未来只会更加拥挤。但你也可以把它看作一个丰盛的语言盛宴。接下来，我们将帮助你理清这场盛宴。

## 17:55-Saron Yitbarek

好吧，我知道这些语言洪流是从哪里来的。但我们如何理解这一切？我们如何挑选出对我们有意义的语言？这是个大问题，所以我请来了一些帮助：Clive Thompson 是理解科技世界的最佳写手之一。他是《连线》的专栏作家、《纽约时报杂志》的特约撰稿人，现在正在写一本关于计算机程序员心理的书。

## 18:24-Saron Yitbarek

这很完美，因为我们需要了解在选择学习哪些语言时，我们大脑里发生了什么。

## 18:31-Saron Yitbarek

接下来是我和 Clive 的讨论。

## 18:35-Saron Yitbarek

当我刚开始作为一名新开发者时，我想：“让我找到最好的语言，我要真正精通它。然后就完成了。”

## 18:44-Saron Yitbarek

但事情并没有那么简单。为什么会有这么多编程语言？

## 18:49-Clive Thompson

每种语言都有其擅长的领域。因此，通常情况下，创建新语言的原因是因为现有语言无法很好地满足某些需求。JavaScript 就是一个很好的例子。

## 19:03-Clive Thompson

在90年代中期，Netscape 创建了一个浏览器，所有这些网站管理员希望能够实现更互动的功能。他们想在网站中有一些脚本功能。

## 19:16-Clive Thompson

于是这些需求传达给了 Netscape。他们意识到：“好吧，我们需要一个脚本语言，而现有的没有办法做到这一点。”

## 19:25-Clive Thompson

于是他们聘请了 Brendan Eich，他当时被认为是个资深人员，32岁，其他人都是21岁。

## 19:32-Saron Yitbarek

在开发者界，这算资深。

## 19:35-Clive Thompson

他们给了他十天的时间来创造 JavaScript。于是他几乎不眠不休，疯狂地编写这个脚本语言。虽然当时的实现有些笨拙且凌乱，但它有效。它允许人们实现一些简单的功能，比如按钮、对话框和弹出窗口。

## 19:54-Clive Thompson

这就是一个新语言的例子，它是为了满足当时无法实现的需求而创建的。

## 20:01-Saron Yitbarek

这真是太有趣了。

## 20:03-Clive Thompson

所以，语言数量众多的原因在于，人们不断发现需要做一些其他语言无法做到的事情。

## 20:11-Saron Yitbarek

让我感兴趣的是，开发者与编程语言之间的关系为何如此强烈，为什么我们对这些工具有如此深的依恋？

## 20:22-Clive Thompson

原因有几个。首先，有时候这只是你学的第一门语言的偶然性，就像你的初恋一样。

## 20:30-Clive Thompson

我认为，不同个性的人与不同类型的语言之间也有某种联系。例如，Facebook 是使用 PHP 开发的，而 PHP 是一种相当复杂的语言，它很不规则，并且在发展的过程中经历了很多波折。这种感觉也反映了 Facebook 的特质。

## 20:49-Clive Thompson

相比之下，谷歌的团队决定：“我们想要一种超级高性能的语言，因为在谷歌，我们非常注重速度，必须支持数万亿用户同时在线。”

## 21:02-Clive Thompson

于是他们决定开发 Go，而 Go 是一种非常适合高性能计算的语言。

## 21:08-Saron Yitbarek

再深入一点说，是我作为开发者，凭借自己的个性，自然会对某些语言产生吸引力？还是说我工作的语言可能会影响我的个性？

## 21:25-Clive Thompson

两者都有。不过，我确实认为，当人们找到自己喜欢的语言时，会产生强烈的共鸣。你进入计算机科学课程，学习的通常都是必修的语言：大家都在教 Java，有时是 JavaScript 或 Python。

## 21:46-Clive Thompson

但关键是，你被迫去学这门语言，所以你就学了。但当人们有选择时，会发生什么？在这里，你可以看到某种情感或心理风格的人如何向某种语言倾斜。我谈到过一个人，他尝试学习 JavaScript 多次。

## 22:03-Clive Thompson

这门语言看起来有点丑陋，括号的使用让人感到困扰。他尝试了又失败，失败了又尝试。然后有一天，他看到一个朋友在用 Python，而 Python 看起来太干净、太美丽了。他是个作家，而这门语言常被认为是适合写作的，因为它的缩进使得一切易于阅读。

## 22:28-Clive Thompson

这让他觉得很契合，因为 Python 的工作方式和外观，那种简约的美，让他产生了共鸣。

## 22:39-Saron Yitbarek

通过与 Clive 的对话，我意识到有些语言是强加于我们的。那些古老的语言，已经融入我们工作的方方面面——就像代码的拉丁语。

## 22:53-Saron Yitbarek

但也有我们选择的语言，那些适合我们个性的语言。如果你想知道什么是新兴的、正在改变游戏规则的语言，就要问问开发者他们周末在用什么。

## 23:05-Saron Yitbarek

这是我们对话的更多内容：

## 23:08-Clive Thompson

当我问人们：“你在空闲时间做什么？”他们往往会提到一些奇怪的东西。我认为这其实是开发者行为中一个很美好、值得称道的特点，他们往往是非常好奇的人。

## 23:22-Clive Thompson

我认识一些人，他们决定：“我就为了好玩，去学 Erlang。”

## 23:26-Saron Yitbarek

我试着想象人们周末正在进行的这些项目，似乎项目本身是次要的。学习工具和语言的过程似乎更重要，真正的目标是这个。

## 23:41-Clive Thompson

正是如此。这就是为什么你会看到人们不断地重复创建日历和待办事项列表，因为这是快速了解语言功能和工作原理的一种方式。只要能建造一些东西，这几乎无关紧要。

## 23:56-Clive Thompson

他们想知道用这种语言思考的感觉。这会不会很简单、令人兴奋，并且流畅，跟我现在使用的语言相比？这会不会打开新的大门，让事情变得更容易？

## 24:13-Clive Thompson

当你遇到一门新语言时，会产生一种可能性空间，这可以非常激动人心，富有想象力。

## 24:20-Saron Yitbarek

作为一个骄傲的 Ruby on Rails 开发者，差不多两年前，另一位知名 Ruby 开发者 Justin Serrals 做了一个很棒的演讲，倡导一种观点：一门语言不需要性感才能被使用。

## 24:41-Saron Yitbarek

他的论点是，Ruby 当时令人兴奋，是因为它新鲜。但几年前它到了一个稳定的成熟阶段，因此不再需要更多的东西。作为成熟语言，它对开发者的吸引力降低，变得不那么新鲜了，我们逐渐转向下一个闪亮的东西。

## 25:05-Saron Yitbarek

从某种意义上说，或许正是我们的好奇心使得一门语言变得不那么吸引人，或许让它有些乏味，无论这门语言本身是好是坏。

## 25:18-Clive Thompson

我完全同意。开发者对新事物的深度好奇和自我教育的渴望，反而导致他们不断寻找新玩意，使用新语言去复制其他语言已经完成得相当好的事情。

## 25:37-Saron Yitbarek

没错。

## 25:37-Clive Thompson

所以就是这样。好奇心是个优点，也是个陷阱。

## 25:43-Saron Yitbarek

是啊，表达得很美。

## 25:49-Saron Yitbarek

有时候，我们的好奇心可能是个陷阱，但它也是推动语言演变的动力。每种新语言的出现都是因为有人说：“如果……会怎样？”开发者想要做一些不同的事情。

## 26:06-Saron Yitbarek

他们想要一种全新的表达方式。

## 26:08-Grace Hopper

我向你们保证。

## 26:11-Saron Yitbarek

我觉得 Grace Hopper 值得最后发言。

## 26:15-Grace Hopper

在接下来的 12 个月里，如果你们中的任何一个人说“我们一直都是这样做的”，我会立刻出现在你身边，缠着你 24 小时。看看我能不能让你再考虑一下。我们再也不能接受这个说法了，这是一种危险的思想。

## 26:34-Saron Yitbarek

Grace Hopper 和第一个编译器的故事提醒我们，总有更好的方法去做某事，只要我们能找到合适的词语。

## 26:43-Saron Yitbarek

无论这些语言变得多么抽象，无论我们是在机器语言的高空还是低空徘徊，我们都需要确保这是一个聪明的选择。我们选择语言，或者甚至构建语言，让我们的意图更接近现实。

## 27:03-Saron Yitbarek

如果你想了解更多关于语言和编译器的知识，你并不孤单。我们整理了一些非常有用的资料，帮助你深入探索。所有资料都在我们的节目备注中，访问 redhat.com/commandlineheroes。

## 27:20-Saron Yitbarek

下一集，我们将追踪开源贡献的复杂路径。维护者面临的真实挑战是什么？我们如何进行第一次 pull request？

## 27:32-Saron Yitbarek

我们将带你进入 Contributing 101。

## 27:39-Saron Yitbarek

《Command Line Heroes》是 Red Hat 的原创播客。可以在 Apple Podcasts、Google Podcasts 或任何你喜欢的平台上免费收听。

## 27:48-Saron Yitbarek

我是 Saron Yitbarek，下次再见，继续编码！
