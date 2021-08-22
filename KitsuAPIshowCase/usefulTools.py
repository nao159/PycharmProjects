class UsefulTools():

    def sort_by(data_to_sort, sort_by):
        """Sorted given dictionary by string key"""
        return sorted(data_to_sort, key=lambda object: object[sort_by])

