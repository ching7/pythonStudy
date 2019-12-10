#  文件操作
#写操作
import pickle
game_data={
    "positon":"N2 E3",
    "pocket":["key","knife"],
    "money":169
}
# w写，b二进制形式
save_file = open("save_dat","wb")
pickle.dump(game_data,save_file)
save_file.close()

#读操作 
# r读，b二进制形式
load_file = open("save_dat","rb")
load_game_data = pickle.load(load_file)
print(load_game_data)
load_file.close()
