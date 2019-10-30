import pkg_resources


def load_plugins(tag):
    plugins = {}

    for ep in pkg_resources.iter_entry_points(group=tag):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        plugin = p()

        plugins[ep.name] = plugin

    return plugins