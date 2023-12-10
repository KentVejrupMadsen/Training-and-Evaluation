from stage      \
    import      \
    training,   \
    evaluation

import launch

def main():
    evaluation()
    training()
    evaluation()


if __name__ == '__main__':
    launch.initialise()
    main()
