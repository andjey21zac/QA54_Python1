# with open("test.txt","w",encoding="utf-8") as file:
#   file.write("Hello")
#   file.write("Alex")

def log_result(test_name,status):
    with open("test_1.txt","a",encoding="utf-8") as file:
        file.write(f"{test_name}:{status}\n")
log_result("test_register","PASSED")
log_result("test_login","FAILED")
log_result("test_log_out","PASSED")





