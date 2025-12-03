# Claude Code + DeepSeek: 多语言 Hello World 示例集合

这个仓库包含了多种编程语言的 Hello World 示例程序，用于快速学习和比较不同编程语言的基础语法。

## 📚 包含的语言

- **C** (`hello_c/`) - 经典的系统编程语言
- **C++** (`hello_cpp/`) - 面向对象的系统编程语言
- **C#** (`hello_cs/`) - .NET 平台的现代面向对象语言
- **Go** (`hello_go/`) - Google 开发的高效并发编程语言
- **Lua** (`hello_lua/`) - 轻量级脚本语言
- **Python** (`hello_py/`) - 简洁优雅的通用编程语言
- **Rust** (`hello_rust/`) - 内存安全的系统编程语言
- **Solidity** (`hello_sol/`) - 以太坊智能合约语言
- **Swift** (`hello_swift/`) - Apple 开发的现代编程语言
- **TypeScript** (`hello_ts/`) - JavaScript 的超集，添加了类型系统

## 🚀 快速开始

### C
```bash
cd hello_c
gcc helloworld.c -o helloworld
./helloworld
```

### C++
```bash
cd hello_cpp
g++ hello.cpp -o hello
./hello
```

### C#
```bash
cd hello_cs
dotnet run
```

### Go
```bash
cd hello_go
go run main.go
# 或编译后运行
go build -o main main.go
./main
```

### Lua
```bash
cd hello_lua
lua hello.lua
```

### Python
```bash
cd hello_py
python hello.py
# 或使用 Python 3
python3 hello.py
```

### Rust
```bash
cd hello_rust
cargo run
# 或编译后运行
cargo build --release
./target/release/hello_rust
```

### Solidity
```bash
cd hello_sol
npm install
npx hardhat compile
npx hardhat test
```

### Swift
```bash
cd hello_swift
swift hello.swift
# 或编译后运行
swiftc hello.swift -o hello
./hello
```

### TypeScript
```bash
cd hello_ts
npm install
npm run build
node dist/index.js
# 或直接运行
npm start
```

## 📋 前置要求

根据你想运行的语言，需要安装相应的编译器或运行时：

- **C/C++**: GCC 或 Clang
- **C#**: .NET SDK
- **Go**: Go 编译器
- **Lua**: Lua 解释器
- **Python**: Python 3.x
- **Rust**: Rust 工具链 (rustc, cargo)
- **Solidity**: Node.js, npm, Hardhat
- **Swift**: Swift 编译器 (macOS 自带或从 swift.org 下载)
- **TypeScript**: Node.js, npm

## 🎯 项目目的

这个项目旨在：

1. 提供多种编程语言的入门示例
2. 方便快速比较不同语言的语法差异
3. 作为学习新编程语言的起点
4. 展示各语言的基本项目结构

## 📝 项目结构

```
.
├── README.md
├── .gitignore
├── hello_c/          # C 语言示例
├── hello_cpp/        # C++ 示例
├── hello_cs/         # C# 示例
├── hello_go/         # Go 示例
├── hello_lua/        # Lua 示例
├── hello_py/         # Python 示例
├── hello_rust/       # Rust 示例
├── hello_sol/        # Solidity 示例
├── hello_swift/      # Swift 示例
└── hello_ts/         # TypeScript 示例
```

## 🤝 贡献

欢迎提交 Pull Request 来添加更多编程语言的示例！

## 📄 许可证: CC0

开源是初级的共产主义，人人共享，人人受益。

## 🔗 相关资源

- [C 语言教程 PDF](https://seriouscomputerist.atariverse.com/media/pdf/book/C%20Programming%20Language%20-%202nd%20Edition%20(OCR).pdf)
- [C++ 参考](https://en.cppreference.com/)
- [C# 文档](https://docs.microsoft.com/dotnet/csharp/)
- [Go 官方文档](https://go.dev/doc/)
- [Lua 官方网站](https://www.lua.org/)
- [Python 官方文档](https://docs.python.org/)
- [Rust 官方教程](https://www.rust-lang.org/learn)
- [Solidity 文档](https://docs.soliditylang.org/)
- [Swift 官方文档](https://swift.org/documentation/)
- [TypeScript 官方文档](https://www.typescriptlang.org/docs/)
