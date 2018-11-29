def print_models(unprint_designs,completed_models):

    while unprint_designs:
        current_design = unprint_designs.pop()
        print(current_design)
        completed_models.append(current_design)

