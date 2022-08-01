source: <https://juejin.cn/post/6844903866128039944>

# iOS异常类型
当你的iOS应用崩溃的时候，我们需要去分析异常日志以定位根本原因。崩溃可能是 “低内存崩溃 Low Memory Crash” 或者 “普通异常崩溃”。当碰到“异常”时，更好的理解“不同类型的异常”能够真正帮助我们快速定位问题所在。
在这篇文章中，我们将研究 iOS 应用可能碰到的不同类型的“异常”，例如EXC_CRASH、EXC_BAD_ACCESS、EXC_RESOURCE、00000020 等。

## 崩溃日志中对异常
“异常”这个词在“崩溃日志”语境下更多与“Mach 异常”（以“EXC_为前缀”）和 “UNIX 信号”（如: SIGSEGV, SIGBUS等）相关。在某些情况下（应该是有对应的dSYM符号文件时）系统会通过映射将底层的 Mach 异常 翻译为 UNIX 信号。这就是为什么你能log中看到有用 “EXC_CRASH(SIGABRT)” 及 “EXC_BAC_ACCESS(SIGSEGV)” 作为 异常类型（Exception Type）。
对于某些异常，还会附带一个关联的 处理器定制异常码（processor-specific Exception Code） 或者 异常子类型（Exception Subtype），用以包含更多问题相关信息。举例来说， “EXC_BAC_ACCESS” 类型异常可能有一行如“KERN_INVALID_ADDRESS at 0x80000010”作为“异常码”； “EXC_RESOURCE” 可能有一行"WAKEUPS"作为"异常子类别"。

## UNIX信号
UNIX信号  | 注释
------------- | -------------
SIGSEGV  | 访问无效的内存地址。地址存在，但是应用程序无法访问。
SIGABRT  | 程序崩溃。由 C函数 abort() 初始化。通常意味着系统检测到某些事务出错，例如 assert() 或者 NSAssert() 校验失败。
SIGBUS  | 访问无效的内存地址。地址不存在，或对齐无效。（The address does not exist, or the alignment is invalid.）
SIGTRAP  | 调试器相关
SIGILL  | 尝试执行非法的、有缺陷、未知的或者需要权限的指令。

更多UNIX信号： <https://en.wikipedia.org/wiki/Signal_(IPC)>

## Mach异常
|Mach异常  | 描述  | 注释 |
| :------------ |:---------------:| :---------------: |
| EXC_BAD_ACCESS  | 错误内存访问 | 访问“错误”内存地址。“错误”可能指“地址不存在”或者“应用没有权限访问”。因此通常与 SIGBUS 及 SIGSEGV 相关联。 |
| EXC_CRASH | 异常跳出 | 通常与 SIGABRT 相关联，意思是由于检测到代码抛出的未捕获异常而使应用程序异常退出。 |
| EXC_BREAKPOINT | 跟踪/断点捕获 | 通用与 SIGTRAP 相关联。可以由你自己的代码或者 NSExceptions 抛出时触发。 |
| EXC_GUARD | 违反了受保护资源的防护（Violated Guarded Resource Protection） | 由违背受保护资源防护触发，例如‘某些文件描述符’ |
| EXC_BAD_INSTRUCTION | 非法指令 | 通常与特定非法或未定义指令/操作数相关。 |
| EXC_RESOURCE | 资源限制 | 应用由于达到资源消耗限制而退出。 |
| 00000020 | 十六进制异常类型 | 非 'OS Kernel' 异常。 |

完整Mach列表：<http://fxr.watson.org/fxr/source/osfmk/mach/exception_types.h?v=xnu-2050.18.24>中(sys/osfmk/mach/exception_types.h)的源码文件。
