import json
import os

def convert_to_chat_format(input_json_path, output_jsonl_path):
    # 读取原始JSON文件
    try:
        with open(input_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        meat_foods = data.get('肉类食物', [])
        if not meat_foods:
            print("错误: 未找到'肉类食物'数组")
            return False
    except Exception as e:
        print(f"读取输入文件失败: {str(e)}")
        return False

    # 转换并写入JSONL文件
    try:
        with open(output_jsonl_path, 'w', encoding='utf-8') as f:
            for idx, item in enumerate(meat_foods):
                # 创建符合要求的对话结构
                messages = [
                    {"role": "system", "content": "你是一个食物信息查询助手，需要提供详细的食物属性说明。"},
                    {"role": "user", "content": f"请告诉我'{item.get('名称', '未知食物')}'的详细属性。"},
                    {"role": "assistant", "content": (
                        f"食物名称: {item.get('名称', '未知')}\n"\
                        f"生命值: {item.get('生命值', 'N/A')}\n"\
                        f"饥饿值: {item.get('饥饿值', 'N/A')}\n"\
                        f"理智值: {item.get('理智值', 'N/A')}\n"\
                        f"描述: {item.get('描述', '无')}"
                    )}
                ]

                # 构建JSON对象
                json_line = {"messages": messages}
                # 写入JSONL行
                json.dump(json_line, f, ensure_ascii=False)
                f.write('\n')

                if idx % 10 == 0:
                    print(f"已处理 {idx+1}/{len(meat_foods)} 条记录")

        print(f"\n转换完成! 输出文件: {output_jsonl_path}")
        print(f"共处理 {len(meat_foods)} 条食物数据")
        return True

    except Exception as e:
        print(f"写入输出文件失败: {str(e)}")
        return False

if __name__ == "__main__":
    # 请将meat_foods.json复制到当前目录(XM文件夹)后再运行
    input_file = "meat_foods.json"
    output_file = "meat_foods_chat.jsonl"

    if not os.path.exists(input_file):
        print(f"错误: 未找到输入文件 '{input_file}'")
        print(r"请先将meat_foods.json复制到当前目录: c:\Users\Lenovo\Desktop\XM")
    else:
        convert_to_chat_format(input_file, output_file)