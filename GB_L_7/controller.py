from calculations import calculation
from ui_c import input_c, output_c
from checks import check_action, check_c
from log import log

inp_list = input_c()
logstr = ';' + 'input' + ';' + str(inp_list)
log(logstr)
while not check_c(inp_list):
    inp_list = input_c()
    logstr = ';' + 'input' + ';' + str(inp_list)
    log(logstr)
func = check_action(inp_list)
logstr = ';' + 'check_action' + ';' + str(func)
log(logstr)
result = calculation(float(inp_list[0]), func, float(inp_list[2]))
logstr = ';' + 'calculation' + ';' + str(result)

output_c(result)

