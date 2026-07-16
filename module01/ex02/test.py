from vector import Vector
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"


try :
	print(f"{BLUE}------vec0 test --------{RESET}")
	vec0 = Vector([[1], [10], [2]])
	print(vec0)
	print(vec0.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec1 test --------{RESET}")
	vec1 = Vector([[1.0], [2.0], [3.0]])
	print(vec1)
	print(vec1.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec2 test --------{RESET}")
	vec2 = Vector((1, 6))
	print(vec2)
	print(vec2.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec3 test --------{RESET}")
	vec3 = Vector (3)
	print(vec3)
	print(vec3.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec4 test --------{RESET}")
	vec4 = Vector ([1, 2, 3])
	print(vec4)
	print(vec4.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec5 test --------{RESET}")
	vec5 = Vector([[1.0, 1.2, 1.3, 1.4]])
	print(vec5)
	print(vec5.shape)
	print(f"{GREEN}--vec5 transpose column to row test --------{RESET}")
	vec5.T()
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")
	
try :
	print(f"{BLUE}------vec6 test --------{RESET}")
	vec6 = Vector([[2.0, 3.2, 4.3, 5.4]])
	print(vec6)
	print(vec6.shape)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{BLUE}------vec7 test --------{RESET}")
	vec7 = Vector([[2.0], [3.2], [4.3], [5.4]])
	print(vec6)
	print(vec6.shape)
	print(f"{GREEN}--vec7 transpose row to column test --------{RESET}")
	vec7.T()
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{CYAN}-----vec5 dot vec 6 test --------{RESET}")
	vec5.dot(vec6)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{CYAN}-----vec5 dot vec 7 test --------{RESET}")
	vec5.dot(vec7)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{CYAN}-----vec5 __add__ vec 7 test --------{RESET}")
	res = vec5.__add__(vec7)
	print(vec5)
	print(vec7)
	print(res)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{CYAN}-----vec5 __sub__ vec 7 test --------{RESET}")
	res = vec5.__sub__(vec7)
	print(vec5)
	print(vec7)
	print(res)
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")

try :
	print(f"{CYAN}-----vec5 __rsub__ vec 7 test --------{RESET}")
	res = vec5.__rsub__(vec7)
	print(vec5)
	print(vec7)
	print(res)
	print(vec7.T().shape)
	print(repr(vec7))
except ValueError as e:
	print(f"{RED}ERROR : {e}{RESET}")