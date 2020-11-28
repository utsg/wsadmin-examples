import sys
import zipfile


# Default install .ear application on IBM WAS with default bindings
# Example: ./wsadmin.sh -lang jython -f install_app.py ~/appname.ear

def get_app_name(path):
    zf = zipfile.ZipFile(path, "r")
    appxml = zf.read("META-INF/application.xml")
    zf.close()

    start_string = "<display-name>"
    end_string = "</display-name>"
    start_index = appxml.find(start_string) + len(start_string)
    end_index = appxml.find(end_string)

    name = appxml[start_index:end_index].strip()

    return name


def install_app(path):
    print("Application for install: %s" % path)
    try:
        AdminApp.install(path, ['-usedefaultbindings', '-useAutoLink'])
    except Exception, exc:
        print("Something goes wrong: %s" % exc)
    print("%s was installed" % path)
    AdminConfig.save()


def update_app(path, name):
    print("Application for update %s" % name)
    AdminApp.update(
        path,
        'app',
        ['-operation', 'update', '-contents', path],
    )
    AdminConfig.save()


try:
    app_path = sys.argv[0]
    app_name = get_app_name(app_path)
    app_list = AdminApp.list().split("\n")

    if app_name in app_list:
        update_app(app_path, app_name)
    else:
        install_app(app_path)
except Exception, ex:
    print("Use command line argument for input application path")
    print(ex)
