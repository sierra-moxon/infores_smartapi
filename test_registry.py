import bioregistry

registry = bioregistry.read_registry()
name = registry.get('name')
homepage = bioregistry.get_homepage(name)
print(name + " " + homepage)
