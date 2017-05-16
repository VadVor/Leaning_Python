import win32com.client as com
from multiprocessing import Pool
from ldap3 import Server, Connection, ALL, SUBTREE


def find_files(connect):
    for entry in connect:
        try:
            ipp = str(entry['attributes']['cn'])
            wmi = com.GetObject(r"winmgmts:{impersonationLevel=impersonate}!\\" + ipp + r"\root\cimv2")
            colfiles = wmi.ExecQuery("Select * from CIM_DataFile where (Drive='C:' or Drive='D:') and (Extension='msi' "
                                     "or Extension='iso')")
            for collect in colfiles:
                with open("d:\\ScanDir\\"+ ipp + str(entry['attributes']['description'])+".txt", "a") as file:
                    file.write(collect.Name+"\n")
                file.close()
        except:
            continue

if __name__ == '__main__':
    total_entries = 0
    server = Server('***', get_info=ALL)
    conn = Connection(server, user="****", password="****", auto_bind=True)
    conn.search(search_base="OU=***,DC=***,DC=bb,DC=***", search_filter="(&(objectCategory=computer)(name=**00*))",
                search_scope=SUBTREE, attributes=['cn', 'description'])
    total_entries += len(conn.response)

    #find_files(conn.response)

    pool = Pool(1)
    pool.map(find_files, conn.response)
    pool.close()
    pool.join()





''' exclude = ['$Recycle.Bin','d:\$RECYCLE.BIN','Windows'] 
for root in ['c:\\', 'd:\\']:
    for folder, subdirs, files in os.walk(root, topdown=True):
        subdirs[:] = [d for d in subdirs if d not in exclude]
        for pattern in ['*.arj', '*.exe', '*.iso', '*.rar', '*.zip', '*.msi', '*.7z', '*.com', '*.mp1', '*.mp2', '*.mp3', '*.mp4', '*.mpg', '*.avi' , '*.mpeg', '*.mkv', '*.flv', '*.wma', '*.mov', '*.asf', '*.7zip']:
            for filename in fnmatch.filter(files, pattern): 
                fullname = os.path.join(folder, filename)
                with open('d:\qqqqqqqq.txt', "a") as file:
                    file.write(fullname+"\n")
file.close() '''
        
    
