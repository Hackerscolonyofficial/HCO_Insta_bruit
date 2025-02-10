from colorama import init
from file.Writer import writer

init()

head = """
\033[34m

		$$\   $$\  $$$$$$\   $$$$$$\      
		$$ |  $$ |$$  __$$\ $$  __$$\     
		$$ |  $$ |$$ /  \__|$$ /  $$ |    
		$$$$$$$$ |$$ |      $$ |  $$ |    
		$$  __$$ |$$ |      $$ |  $$ |    
		$$ |  $$ |$$ |  $$\ $$ |  $$ |    
		$$ |  $$ |\$$$$$$  | $$$$$$  |    
		\__|  \__| \______/  \______/     

		 $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\      $$\
		\__$$  __|$$  _____|$$  __$$\ $$$\    $$$ |
		   $$ |   $$ |      $$ /  $$ |$$$$\  $$$$ |
		   $$ |   $$$$$\    $$$$$$$$ |$$\$$\$$ $$ |
		   $$ |   $$  __|   $$  __$$ |$$ \$$$  $$ |
		   $$ |   $$ |      $$ |  $$ |$$ |\$  /$$ |
		   $$ |   $$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |
		   \__|   \________|\__|  \__|\__|     \__|
"""
sub_head = """
\033[32m

          _______  _______   _________ _______  _______  _______ 
|\     /|(  ____ \(  ___  )  \__   __/(  ____ \(  ___  )(       )
| )   ( || (    \/| (   ) |     ) (   | (    \/| (   ) || () () |
| (___) || |      | |   | |     | |   | (__    | (___) || || || |
|  ___  || |      | |   | |     | |   |  __)   |  ___  || |(_)| |
| (   ) || |      | |   | |     | |   | (      | (   ) || |   | |
| )   ( || (____/\| (___) |     | |   | (____/\| )   ( || )   ( |
|/     \|(_______/(_______)     )_(   (_______/|/     \||/     \|
                                                                 

"""


def Heading():
    writer(head)

def Sub_head():
    writer(sub_head)

if __name__ == "__main__":
    Heading()
    Sub_head()
