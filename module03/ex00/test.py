from NumPyCreator import NumPyCreator

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

if __name__ == "__main__":
	npc=NumPyCreator()
	print(f"npc.from_list([[1,2,3],[6,3,4]]) : \n {GREEN}{npc.from_list([[1,2,3],[6,3,4]])}{RESET}")
	print(f"npc.from_list([[1,2,3],[6,4]]) : \n {GREEN}{npc.from_list([[1,2,3],[6,4]])}{RESET}")
	print(f"npc.from_list([[1,2,3],[’a’,’b’,’c’],[6,4,7]]) : \n {GREEN}npc.from_list([[1,2,3],[’a’,’b’,’c’],[6,4,7]]){RESET}")
	print(f"npc.from_list(((1,2),(3,4))) : \n {GREEN}{npc.from_list(((1,2),(3,4)))}{RESET}")
	print(f'npc.from_tuple(("a", "b", "c")) : \n {GREEN}{npc.from_tuple(("a", "b", "c"))}{RESET}')
	print(f'npc.from_tuple(["a", "b", "c"]) : \n {GREEN}{npc.from_tuple(["a", "b", "c"])}{RESET}')
	print(f"npc.from_iterable(range(5)) : \n {GREEN}{npc.from_iterable(range(5))}{RESET}")
	shape=(3,5)
	print(f"npc.from_shape(shape) : \n {GREEN}{npc.from_shape(shape)}{RESET}")
	print(f"npc.random(shape) : \n {GREEN}{npc.random(shape)}{RESET}")
	print(f"npc.identity(4) : \n {GREEN}{npc.identity(4)}{RESET}")
