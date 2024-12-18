# 创建 JavaScript

一项旨在在万维网早期阶段设定方向的使命。十天内完成。结果？一种不可或缺的语言，改变了一切。

JavaScript 是在逆境中获胜的黑马。Clive Thompson 回顾了浏览器大战，以及其影响如何塑造了互联网的未来。Charles Severance 解释了 JavaScript 如何从一次临时的冒险变成默认的网页开发语言。Michael Clayton 坦承，他和许多人一样，低估了 JavaScript。而 Klint Finley 则描述了一个没有它的阴郁互联网。

## 00:00-Saron Yitbarek

大家好，我们回来了。我们很高兴推出《命令行英雄》第三季。我们要感谢许多人，因为这个节目中的故事都是从与开发者、系统管理员、IT 架构师、工程师以及开源社区的人士的交谈开始的，讨论你们最感兴趣的话题和技术。现在，我们想进一步开放这个方式。我们希望你们所有人都能参与进来，帮助塑造《命令行英雄》的未来。你可以通过填写我们的短期调查来做到这一点。你喜欢这个节目什么？你希望我们多聊些什么？亲爱的听众，我们想了解更多关于你的信息。你是开发者吗？你在运营方面工作，还是从事与技术世界完全无关的工作？请访问 commandlineheroes.com/survey，帮助我们提升第四季及以后节目的质量。现在，开始第三季。

## 01:00-Saron Yitbarek

Brendan Eich 在 34 岁时坐在 Netscape 总部的桌子前。他承诺进行一次为期 10 天的编码冲刺。仅在 10 天内创造一种全新的编程语言。那是 1995 年，编程语言的世界即将永远改变。

## 01:26-Saron Yitbarek

我是 Saron Yitbarek，这里是《命令行英雄》，Red Hat 的原创播客。在整个季节中，我们将探索编程语言的力量和承诺，发现我们的语言如何塑造了开发世界，以及它们如何增强我们的工作。这一次，我们追踪 JavaScript 的创建。也许你听过 Brendan Eich 的故事，但像 JavaScript 这样的东西到底是如何被创造出来的？当然有 Brendan 的冲刺，但故事远不止于此。

## 02:02-Saron Yitbarek

我们的 JavaScript 故事始于一场战争，一场浏览器战争。1990 年代的浏览器战争可能看似历史，但其后果却极其重要。在战场的一方是 Netscape，它与 Sun Microsystems 结成了联盟。另一方是软件巨头微软。他们争夺的是什么？这是一场决定谁将成为互联网守门人的战斗。赌注大得不可想象。

## 02:40-Saron Yitbarek

要真正理解浏览器战争是如何展开的，我联系了我最喜欢的技术历史学家之一，作家 Clive Thompson。他最近的书是——

## 02:50-Clive Thompson

《程序员：新部落的形成与世界的重塑》。

## 02:54-Saron Yitbarek

Clive 和我谈到了浏览器战争，但让我为你真正设定场景。Netscape 意识到浏览器是人们上网所需的关键软件。而微软，他们的整个商业模式是将东西打包到 Windows 中。他们在 1990 年代之前并没有真正关注浏览器，直到微软意识到他们可能一直在睡觉。世界正在转向在线，而微软 Windows 中没有任何东西能帮助他们到达那里。但这些人，某个叫 Netscape 的公司，正在提供通往互联网的桥梁。突然之间，微软的行业主导地位看起来就不那么绝对了。浏览器战争就在那一刻开始了，微软意识到互联网的力量，眯起眼睛盯着他们的新竞争对手。好了，以上是我的背景介绍。接下来是我和 Clive 讨论接下来发生了什么。

## 04:03-Clive Thompson

这场争斗是关于谁将成为上网的主要入口。你必须明白，在 90 年代初，几乎没有人真正在线。当 Mosaic 出现并最终变成 Netscape 时，它是第一个任何人都可以下载的浏览器，允许你浏览网络。他们在 1994 年 12 月上线。突然之间，成千上万甚至数百万的人能够以这种图形化的方式使用互联网。他们的下载量和媒体关注度都达到了惊人的水平。每个人基本上都在说，“是的，Netscape 算是这个叫做互联网的东西的未来。”

## 04:40-Clive Thompson

所以在西雅图，微软以极大的 alarm 关注这一切，因为他们几乎忽视了互联网。他们专注于销售 Windows，并且没有真正关注这个叫做互联网的疯狂新事物。因此，他们不得不进行一次非常快速的追赶游戏。他们自己的浏览器几乎晚了一年才推出。1995 年秋天，他们的浏览器发布，这基本上标志着浏览器战争的开始，那一刻微软试图争夺成为人们上网的入口。

## 05:13-Saron Yitbarek

好吧。一年时间来赶上并不算太糟糕，对吧？这听起来不算太长。对吧？这似乎是合理的时间。

## 05:21-Clive Thompson

不，这确实听起来不算长，但当时的发展速度非常快。而且有一种强烈的先发优势的感觉，第一家公司能够以某种方式建立自己的品牌，成为人们上网的方式，几年乃至永远都会是赢家。我记得当时发展速度有多快。我是说，Netscape 每几个月就推出一个新浏览器，对吧？他们会说，“哇，我们现在将电子邮件集成到浏览器中。现在，我们有一个小搜索栏。”它不断变得越来越好。你可以看到，所有你可以在线上做的事情都在迅速浮现。

## 06:01-Clive Thompson

微软习惯于非常缓慢地开发。这里是一个长达四年的开发过程，最后出来的是尽可能没有错误的版本。把它放进盒子里，送到商店，而我们四年不发布新版本。Netscape 来了，它是第一家公司说：“不，我们会发布一种次标准的产品，但它足够好用，我们会在三个月内推出一个新版本，三个月、三个月、三个月。”这完全打乱了微软的节奏。

## 06:30-Saron Yitbarek

好吧。所以如果我是微软，我可以看着这一切说，“哦，我的天，这就是未来。我需要赶上。我需要竞争。”或者我可以说，“啊，这只是一个潮流。”那么是什么让微软选择了第一种选择？是什么让微软意识到，“哦，我的天，这真的是个大事情。我需要竞争。”

## 06:51-Clive Thompson

关于浏览器的问题在于，它具有巨大的文化价值。这是你在互联网上可以做的第一件像文化上有趣的事情。你可以突然访问一个乐队的网页，看到他们的帖子和照片。你可以通过找到佛罗里达州的模型火车爱好者来研究你的爱好，对吧？所以，在此之前，互联网的一切看起来都很书呆子。电子邮件、文件传输等等。突然间，浏览器让互联网看起来像一本杂志，像一种有趣的互动方式。报纸、CNN 和杂志第一次以如此兴奋的方式写关于它的文章。这是技术从商业版的深处移动到《纽约时报》 A1 页面的时刻。

## 07:41-Saron Yitbarek

那么，对于开发者来说，Netscape 或者浏览器本身有什么吸引力？他们为什么如此热衷？

## 07:48-Clive Thompson

我遇到过很多开发者。突然间，互联网随着浏览器的出现而出现，你可以拥有一个网页，上面写着“快来下载我的酷软件。”所以，它解锁了我们今天看到软件制作的整个世界。

## 08:04-Saron Yitbarek

我应该提到的是，微软最初确实提出收购 Netscape。虽然他们提供的金额非常小，但 Netscape 拒绝了他们。因此，微软不得不自己开发一个浏览器。他们称自己的浏览器为 Explorer。

## 08:21-Clive Thompson

微软花了一年时间疯狂地开发浏览器，并在 1995 年秋天推出了它。他们所做的基本上和 Netscape 一样。他们快速推出了一款产品，而不担心它是否完美，之后逐渐改进。然而，在 90 年代后半期，真正出现的战争是关于哪个浏览器会更有趣、更具互动性和复杂性。

## 08:53-Saron Yitbarek

请记住，Netscape 在这场斗争中并没有占上风。

## 08:57-Clive Thompson

微软处于非常强大的位置。当你的 Windows 系统在全球约 80% 到 90% 的计算机上出货时，使你的软件成为默认选项是相当容易的。这正是他们所做的。因此，你可以看到 Explorer 不断上升。

## 09:16-Saron Yitbarek

在某种程度上，可怜的 Netscape 始终是这场战斗中的黑马，但事情是这样的。在战斗还未结束之前，他们抛出了一个精彩的绝招，结果证明这对整个编程世界来说是个了不起的分数。

## 09:35-Clive Thompson

这就是 JavaScript 创造的迷人而奇怪的故事。

## 09:43-Saron Yitbarek

围绕网络和浏览器潜力的所有热潮让一件事情变得非常明确。我们需要一种新的编程语言，远远超越 HTML。我们需要一种专门为所有新的基于网络的开发量身定做的语言。我们希望一种不仅能在网上生存，而且能在网上蓬勃发展的语言。

## 10:10-Clive Thompson

你如何为浏览器创建一种编程语言？

## 10:15-Saron Yitbarek

我的朋友，这就是十亿美元的问题。因此，当 Netscape 意识到微软在与他们竞争时，他们开始关注 Java™。Java 是否会成为网络开发的语言？Java 是一种丰富的编译语言。它的性能与 C++ 一样出色。但它仍然需要编译。开发者真正想要的是更轻量级的东西，一种可以被解释而不是编译的语言，一种能够吸引那些涌向网络的非专业程序员的语言。毕竟，那些新程序员希望直接在网页上工作。这就是梦想。

## 11:05-Saron Yitbarek

Netscape 需要一种可以在他们的浏览器中运行的编程语言，这种语言能够让开发者为那些静态网页赋予生命。他们想，如果能在发布 Netscape 2.0 的 beta 版时同时推出一种新的轻量级语言，能为网络编程带来奇迹，那该多好。然而，唯一的问题是。这正好给他们 10 天的时间来创建一种新语言。实际上，这给了一个人，Brendan Eich，10 天的时间。他就是负责这一任务的人。毫无疑问，如果有人能做到，这个人就是他。当 Brendan 在伊利诺伊大学读书时，他曾经出于好玩而创建新语言，仅仅是为了玩玩语法。

## 11:57-Charles Severance

Brendan Eich 的关键在于，当他创建 JavaScript 时，他已经成为某种语言迷。

## 12:05-Saron Yitbarek

为了理解 Eich 实际上做了什么，我们联系了密歇根大学信息学院的教授 Charles Severance。

## 12:14-Charles Severance

JavaScript 的创建环境是这样的：当时 Java 被视为未来，因此在 1994 年，我们认为它会解决一切。仅仅一年后，实际上会解决一切的东西即将出现，但它不能说，“嘿，我解决了一切”，因为每个人，包括我自己，在 1994 年和 1995 年都相信我们已经看到了摇滚乐的未来，而那就是 Java 编程语言。他们必须构建一种看起来无关紧要、看起来愚蠢、看起来毫无意义的语言，而这恰恰是正确的解决方案。

## 12:56-Saron Yitbarek

然而，Eich 提供的并不仅仅是一个玩具语言。它在隐秘的方式上很复杂，借鉴了之前语言的重大灵感。

## 13:07-Charles Severance

如果你查看基本语法，很明显它受到 C 语言的启发，有着大括号和分号。一些字符串模式是来自 Java 编程语言，但底层的面向对象模式则来源于一种叫做 Modula-2 的编程语言，它有着一等公民函数的概念，对我来说，这确实是让 JavaScript 成为如此强大和可扩展语言的最令人惊讶的选择之一，也就是说，函数本身的主体，构成函数的代码也是数据。

## 13:41-Charles Severance

另一个真正成为灵感来源的东西是 HyperCard。JavaScript 始终在浏览器中运行，这意味着它有着文档对象模型的基本数据上下文，这是一种网页的面向对象表示。它与传统的编程语言不同。JavaScript 代码不是从头开始的。它首先是一个网页，因此它最终呈现出这种事件驱动的编程。

## 14:12-Saron Yitbarek

当 JavaScript 与 Netscape Navigator 2.0 一起于 1995 年 11 月 30 日发布时，所有的魔力都汇聚成了一种强大的小语言种子。包括美国在线和 AT&T 在内的 28 家公司同意将其作为一种开放标准语言发布。发布时，一些老前辈对此嗤之以鼻，认为 JavaScript 只是新手的语言。他们忽视了它的革命潜力。

## 14:46-Charles Severance

Brendan 决定把一些不太为人所知的高级概念偷偷地融入到这种语言中，这些概念非常像高级面向对象语言。因此，JavaScript 几乎就像一个特洛伊木马。它悄悄地进入了我们的集体意识，带着一种看似愚蠢、好玩、简单且轻量的形象。但从一开始就内置了一个强大而深思熟虑的编程语言，能够做到计算机科学中几乎所有的事情。

## 15:17-Saron Yitbarek

结果是一种本土于浏览器的语言，能够随着我们在线生活的演变而发展。没过多久，JavaScript 就成为了事实上的网页开发选择。

## 15:29-Charles Severance

JavaScript 是一种我必须学习的语言，实际上学习 JavaScript 的人通常没有选择，因为他们会说，“我想构建一个浏览器应用程序，并希望它具有互动元素。”因此，答案就是你必须学习 JavaScript。如果你想象一下，你最喜欢的语言是什么，答案几乎肯定是 x 加上 JavaScript，对吧？有人可能会说：“我喜欢 Python 和 JavaScript，”或者“我喜欢 Scala 和 JavaScript，”因为这是一种每个人都必须学习的语言。

## 16:05-Saron Yitbarek

Charles Severance 是密歇根大学信息学院的教授。Netscape 从一开始就表现得非常强劲，并在浏览器战争中奋力拼搏，但最后 ...

## 16:22-Clive Thompson

Netscape 作为一个严肃产品就此消失了。

## 16:27-Saron Yitbarek

微软在整个行业的统治是一个压倒性的力量。尽管他们在浏览器竞争中晚了一年，但他们能够重新夺回顶部并赢得这场斗争。但你知道，Netscape 的绝地反击，它的 JavaScript 创造，是一个成功，因为在斗争结束很久之后，这颗从他们的浏览器战争中诞生的珍珠语言将拥有改变一切的余生。

## 17:01-Saron Yitbarek

如果你最近才开始编码，你可能会认为能够开发互动网页，实时更改和更新，而不需要从服务器上获取整个页面的新副本是一种理所当然的事。但想象一下，当这成为一个全新选项时是什么样子。我们请到了 Red Hat 的软件工程师 Michael Clayton，帮助我们理解这是一种多么巨大的转变。

## 17:28-Michael Clayton

我想在 2004 年，Google Mail 发布了 Gmail。据我所知，这是第一个真正将 JavaScript 提升到下一个水平的网络应用程序，它使用 JavaScript 动态切换你所查看的内容。

## 17:49-Saron Yitbarek

比如说你正在查看收件箱，然后你点击一封邮件。在过去，你的邮件查看器需要在浏览器中加载一个全新的页面来显示那封邮件。然后你关闭邮件，整个收件箱又会重新加载。

## 18:05-Michael Clayton

这造成了很多延迟。当你在不同视图之间切换时，等待的时间很多，而 Gmail 改变了这一切。他们使用 JavaScript 在后台获取你想要查看的内容，然后直接展示给你，而不需要你等待一个全新的页面视图。

## 18:23-Saron Yitbarek

这节省了大量的时间和精力。但实际上，仔细想想，这不仅仅改变了速度。它改变了我们工作的本质。

## 18:35-Michael Clayton

因此，网页开发者的职位从一个服务器端、幕后角色转变为距离用户只有一层薄薄的隔离，因为他们是在用户查看网页的浏览器中直接编写代码。

## 18:52-Saron Yitbarek

这一切都改变了。实际上，你可以说 JavaScript 促成了 Web 2.0 革命。任何拥有网页浏览器的人突然之间都有了一个开发环境就在眼前。但是，正如我之前提到的，旧一代人并不一定对这种民主化的趋势感到舒适。

## 19:16-Michael Clayton

我自己也是早期对 JavaScript 怀有敌意的人。我曾经有浏览器扩展来防止 JavaScript 运行。我认为它是一种无用的玩具语言，每当我访问一个需要 JavaScript 才能实现某些关键功能的网站时，我都会感到愤怒。我会想：“你应该以正确的方式构建网站，而不需要 JavaScript。”

## 19:43-Saron Yitbarek

不过，很快，Brendan Eich 的这门十天语言固有的美丽和潜力变得显而易见。而现在，它不仅征服了浏览器，还征服了服务器。随着 Node.js 的出现，这门小语言的潜力开启了一个全新的领域。

## 20:03-Michael Clayton

当我听说 JavaScript 将在服务器上运行时，我想：“为什么会有人想这样做？”到那时，我已经是一名专业的 JavaScript 开发者了。我每天写很多 JS，但我仍然不太明白为什么它适合在服务器上运行。结果，正如许多听众所知道的，Node.js 现在在行业中是一个巨大的力量。我认为这是有充分理由的。

## 20:32-Michael Clayton

Node.js 成功的一个原因是它利用了庞大的前端 JavaScript 开发者社区，即客户端开发者。他们编写代码，为浏览器编写 JavaScript。这些开发者有很多，通过让相同的编程语言可以用于编写服务器，他们立即拥有了一大批可以开始为服务器做贡献的人。这个工具已经在你的工具箱里，你只需拿出来，安装 Node.js，就可以开始了。

## 21:11-Saron Yitbarek

首先在浏览器中，然后在服务器上。JavaScript 是一种不事张扬、秘密优雅、偶尔有些 bug 的语言。它是浏览器战争中的幸存者，大家都低估了它。

## 21:25-Michael Clayton

JavaScript 的故事有点像灰姑娘，起初是在短短 10 天内匆忙拼凑起来的，经历了来自其他编程社区的许多嘲讽，但仍然以某种方式继续找到成功与增长，现在 JavaScript 要么是世界上最流行的编程语言之一，要么是第二名。JavaScript 几乎无处不在。它能在网页中运行意味着 JavaScript 与网络一样普遍，而网络本身就是非常普遍的。

## 22:08-Saron Yitbarek

Michael Clayton 是 Red Hat 的一名工程师。JavaScript 是否“吞噬”了世界？它是否借助网络的东风达到了语言主导地位？我想了解 JavaScript 的边界到底在哪里。

## 22:25-Klint Finley

嗨，我叫 Klint Finley。我是 Wired.com 的一名作家。

## 22:28-Saron Yitbarek

Klint 对同样的事情感到好奇。他越是研究 JavaScript 如今的运行方式，就越发现它已经渗透到他在线生活的每个角落。

## 22:40-Klint Finley

JavaScript 已经成为可以在你甚至还没来得及决定是否要在你的计算机上运行这些不同应用程序之前，就能赋能整个应用程序的东西。它们就开始运行，有些与广告有关，或是促进广告商使用的跟踪功能。所以，在你的浏览器中，有很多事情在悄然发生，而你可能甚至都不知道或不希望它们发生。

## 23:07-Saron Yitbarek

于是 Klint 决定做一个小实验。

## 23:10-Klint Finley

我决定尝试一下在没有 JavaScript 的情况下使用网络。我决定尝试一周，在浏览器中禁用 JavaScript。

## 23:21-Saron Yitbarek

听起来很简单，但放弃所有 JavaScript 产生了一些令人惊讶的效果。因为 JavaScript 已经变得如此庞大，如此全能，这个以轻量著称的语言实际上现在占用了大量空间和能量。当 Klint 阻止了这个语言时……

## 23:39-Klint Finley

总体来说，从页面加载速度、页面的简洁度、电脑电池续航时间等多个方面来说，体验要好得多。而且我感觉对电脑上发生的事情有了更多的控制，因为不再有那些奇怪的、不可见的随机程序在后台运行。

## 24:02-Saron Yitbarek

想象一下，第一次没有弹出广告的生活是多么美好。

## 24:07-Klint Finley

很多内容依赖 JavaScript 才能加载。因此，网页变得简单得多，广告减少了，干扰也少了。

## 24:17-Saron Yitbarek

但无广告的网页体验并不是全部。如果你禁用 JavaScript，网络的某些部分根本无法运作。

## 24:26-Klint Finley

很多东西根本无法使用。Gmail 会把我重定向到一个我认为是为老式手机设计的版本。Facebook 也有类似的情况，许多流畅的交互不复存在，变得更像是一系列网页。Netflix 无法运行，YouTube 也不行。是的，任何严重依赖交互的东西都无法运行。最终，禁用 JavaScript 有好有坏，我不得不决定有 JavaScript 比完全没有要好。

## 25:05-Saron Yitbarek

Klint Finley 是 Wired.com 的一名撰稿人。大多数人预测，JavaScript 将继续主导移动端和桌面应用程序的开发。浏览器游戏、浏览器艺术项目等的复杂性正在飞速提升，而不断壮大的 JavaScript 社区也在最大限度地发挥这一潜力。

## 25:34-Saron Yitbarek

此时我们值得回顾一下，1995 年，也就是几十年前，Brendan Eich 坐在一个房间里，敲打着一个新语言。而今天，这个语言已渗透到我们所做的一切中。说某段新的代码将会改变世界可能听起来有些陈词滥调，但这种事情确实发生过。一位命令行英雄将他们对语言的全部热爱汇聚到一个 10 天的冲刺中，而世界的 DNA 从此被永远改变。

## 26:10-Saron Yitbarek

我们可以感谢 JavaScript 带来了 Google Docs、YouTube 和 Netflix。但你知道，“能力越大，责任越大”，随着 JavaScript 影响力的持续增长，由大量开源库推动，这份责任不再只落在一个人身上。一个更广泛的社区已经掌控了方向。SlashData 最近估计 JavaScript 开发者的数量为 970 万，而在 GitHub 上，JavaScript 的 pull 请求比任何其他语言都多。力量现在掌握在整个命令行英雄的世界手中，他们帮助 JavaScript 在我们开发未来时不断成长。

## 26:59-Saron Yitbarek

下次，命令行英雄将陷入一个语言的网络，我们会探索 Perl 如何在一个崭新的领域中蓬勃发展。

## 28:04-Saron Yitbarek

最后，有一位听众分享了我们上一季的 "Hello World" 集，当时我们也谈到了 Brendan Eich 和 JavaScript。在那期节目中，一位嘉宾说 Brendan 可能在那 10 天里几乎没有睡觉。Brendan 后来在 Twitter 上回应说，在那段冲刺中，他确实有睡觉。如果你想了解那 10 天发生了什么，可以去收听 Devchat 播客中与 Brendan 的采访。我们会在节目笔记中附上链接。我是 Saron Yitbarek。下次见，继续编码吧。
