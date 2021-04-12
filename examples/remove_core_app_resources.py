
# Remove JDBCProvider, JAASAuthData, ActivationSpecs, ConnectionFactories, WMQQueues, WMQTopics
# Example: ./wsadmin.sh -lang jython -f remove_core_app_resources.py

def clear_resource_list(list):
    for item in list:
        print("Remove %s" % item)
        AdminConfig.remove(item)
    AdminConfig.save()


try:
    server_id = AdminConfig.getid("/Server:server1")

    clear_resource_list(AdminUtilities.convertToList(AdminConfig.list('JDBCProvider')))
    clear_resource_list(AdminUtilities.convertToList(AdminConfig.list('JAASAuthData')))
    clear_resource_list(AdminUtilities.convertToList(AdminTask.listWMQActivationSpecs(server_id)))
    clear_resource_list(AdminUtilities.convertToList(AdminTask.listWMQConnectionFactories(server_id)))
    clear_resource_list(AdminUtilities.convertToList(AdminTask.listWMQQueues(server_id)))
    clear_resource_list(AdminUtilities.convertToList(AdminTask.listWMQTopics(server_id)))
    clear_resource_list(AdminUtilities.convertToList(AdminConfig.list("WorkManagerInfo")))

except Exception, ex:
    print("Something goes wrong!\n%s" % ex)
