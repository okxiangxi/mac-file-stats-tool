import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_files_in_folder():
    """带错误捕获的文件统计脚本，出错会弹窗提示"""
    try:
        # 第一步：弹出调试提示，确认脚本启动
        messagebox.showinfo("调试", "脚本已启动，准备选择文件夹")
        
        # 隐藏tkinter空白窗口
        root = tk.Tk()
        root.withdraw()
        
        # 选择文件夹
        folder_path = filedialog.askdirectory(title="选择要统计的文件夹")
        if not folder_path:
            messagebox.showinfo("提示", "未选择文件夹，程序退出")
            return
        
        # 第二步：弹窗确认选中的文件夹
        messagebox.showinfo("调试", f"已选中文件夹：{folder_path}")
        
        # 统计文件/文件夹数量
        file_count = 0       # 纯文件数
        folder_count = 0     # 子文件夹数
        for root_dir, dirs, files in os.walk(folder_path):
            folder_count += len(dirs)
            file_count += len(files)
        total_count = file_count + folder_count
        
        # 弹窗显示结果（三引号完整闭合！）
        result_text = f"""统计完成！
📁 选中文件夹：{folder_path}
📄 纯文件总数（含子文件夹）：{file_count}
📁 子文件夹总数（含子文件夹）：{folder_count}
🔢 总项目数（文件+文件夹）：{total_count}"""  # 这里的"""必须存在，不能漏
        messagebox.showinfo("文件数量统计结果", result_text)
    
    except Exception as e:
        # 出错时弹窗显示错误信息（关键！定位问题）
        messagebox.showerror("运行出错", f"错误原因：{str(e)}")

if __name__ == "__main__":
    count_files_in_folder()