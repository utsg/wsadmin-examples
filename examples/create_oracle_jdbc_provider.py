import sys


# Default install oracle jdbc provider with default bindings
# Example: ./wsadmin.sh -lang jython -f create_oracle_jdbc_provider.py OracleJDBC /usr/JDBCHome/ojdbc8.jar

def create_jdbc_provider(cell_name, driver_classpath, driver_name):
    AdminTask.createJDBCProvider(
        '[-scope Cell=%s -databaseType Oracle -providerType "Oracle JDBC Driver"'
        '-implementationType "Connection pool data source" -name "%s" -classpath "%s"]' % (
            cell_name, driver_name, driver_classpath)
    )
    AdminConfig.save()


try:
    cell = (AdminConfig.list("Cell").split("("))[0]
    jdbc_name = sys.argv[0]
    jdbc_path = sys.argv[1]
    create_jdbc_provider(cell, jdbc_path, jdbc_name)
except Exception, ex:
    print("Use command line arguments for input:\n1) ProviderName\n2) JDBC driver path ")
    print(ex)
