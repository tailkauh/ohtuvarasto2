class Project:
    def __init__(self, tool_dict):
        self.name = tool_dict['name']
        self.description = tool_dict['description']
        self.license = tool_dict['license']

        self.authors = tool_dict['authors']
        
        self.dependencies = tool_dict['dependencies']
        
        self.dev_dependencies = tool_dict['group']['dev']['dependencies']

    def _stringify_list(self, ls):
        return "\n- " + "\n- ".join(ls)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            "\n"
            f"\nAuthors: {self._stringify_list(self.authors)}"
            "\n"
            f"\nDependencies: {self._stringify_list(self.dependencies)}"
            "\n"
            f"\nDevelopment dependencies: {self._stringify_list(self.dev_dependencies)}"
        )
