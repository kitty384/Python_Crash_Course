def print_modes(unprinted):
    complete_models = []
    while unprinted:
        current_design = unprinted.pop()
        print("\nPrinting model:" + current_design)
        complete_models.append(current_design)
    return complete_models
