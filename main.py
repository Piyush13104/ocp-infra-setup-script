
import getpass
import subprocess
import sys



def regitser_system() -> bool:
    rhn_id = input("Enter rhn Id:")
    password = getpass.getpass("Passowrd:")

    if id == "" or password == "":
        print("Id Passoword required...")
        sys.exit(1)
    
    result = ""
    try:
        result = subprocess.run(
            [
                "subscription-manager", 
                "register", 
                "--username", rhn_id, 
                "--password", password
            ],
            capture_output=True,  
            text=True,            
            check=True        
        )
        print(result)
        return True
    except:
        print("Failed to register incorrect id or password..")  
        return False  



def install_dependencies()->bool:

    pass


def firewall_ports_services_add():

    pass

def setup_dns():

    pass

def setup_load_balancer():

    pass


def setup_apache_server():

    pass


def run_scripts():

    try: 
        result = regitser_system()
        if result:
            print("Register Successfull..")
        else:
            print("ERROR: Not able to register..")
    except:
        print("FAILED: Failed while registering system...")


    try:
        result = install_dependencies()
        if result:
            print("Dependencies Installed")
        else:
            print("ERROR: Failed to installed dependies")
    except:
        print("FAILED: Failed while Installing Dependencies...")


    try: 
        result = firewall_ports_services_add()
        if result:
            print("Firewall updated")
        else:
            print("ERROR: Failed firewall setup")
    except:
        print("FAILED: Failed while Adding firewall Ports & services...")
    

    try: 
        result = setup_dns()
        if result:
            print("DNS setup done")
        else:
            print("ERROR: Failed to set DNS")
    except:
        print("FAILED: Failed while Dns setup...")


    try: 
        result = setup_load_balancer()
        if result:
            print("Load Balancer setup done ")
        else:
            print("ERROR: Failed to Setup LoadBalancer")
    except:
        print("FAILED: Failed while setup load balancer...")

    
    try: 
        result = setup_apache_server()
        if result:
            print("Apache server Setup done")
        else:
            print("ERROR: Failed to Setup  Apache server")
    except:
        print("FAILED: Failed while setup apache server...")



if __name__=="__main__":
    run_scripts()