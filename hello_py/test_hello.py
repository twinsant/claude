import subprocess
import sys

def test_hello_output_subprocess():
    """测试 hello.py 输出 'Hello, World!' (使用子进程)"""
    # 使用子进程运行 hello.py 并捕获输出
    result = subprocess.run(
        [sys.executable, "hello.py"],
        cwd=".",  # 当前目录
        capture_output=True,
        text=True
    )
    # 检查标准输出
    assert result.stdout == "Hello, World!\n"
    # 检查标准错误为空
    assert result.stderr == ""
    # 检查返回码为0（成功）
    assert result.returncode == 0

def test_hello_output_capsys(capsys):
    """测试 hello.py 输出 'Hello, World!' (使用 pytest capsys fixture)"""
    # 清空之前的输出缓冲区
    capsys.readouterr()

    # 导入模块会执行 print 语句
    # 如果模块已经导入过，需要先删除再导入以确保执行
    import sys
    if 'hello' in sys.modules:
        del sys.modules['hello']
    import hello # noqa: F401

    # 捕获输出
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
    assert captured.err == ""