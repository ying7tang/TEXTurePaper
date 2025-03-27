import trimesh
import os

cur_dir = 'shapes/'

filename = 'OEPN5LUR_lower.obj'

# 加载OBJ文件
mesh = trimesh.load_mesh(os.path.join(cur_dir, filename))

# 检查模型是否是水密的
if mesh.is_watertight:
    print("模型是水密的，不需要修复。")
else:
    print("模型不是水密的，正在进行修复...")

    mesh.fill_holes()  # 填补孔洞
    mesh.remove_unreferenced_vertices()  # 删除未使用的顶点
    mesh.process()  # 处理三角面连接问题


    new_name = filename.split('.')[0] + '_fixed.obj'

    # 保存修复后的模型
    mesh.export(os.path.join(cur_dir, new_name))
    print("修复后的模型已保存为：", new_name)
