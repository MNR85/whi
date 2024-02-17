import docker
client = docker.from_env()  
def create(**kwargs):    
    res={}
    try:
        res=client.containers.create(**kwargs)                
    except Exception as error:
        res={"status":"failed", "error":error}         
    finally:
        return res
def delete(id_or_name):
    res={}
    try:
        container = client.containers.get(id_or_name)
        # Remove the container
        res=container.remove(force=True)              
    except Exception as error:
        res={"status":"failed", "error":error}         
    finally:
        return res
# def run(**kwargs):
#     client = docker.from_env()
#     print("Docker run: ", kwargs.items)
#     res=client.containers.run(**kwargs)
#     print("res", res)