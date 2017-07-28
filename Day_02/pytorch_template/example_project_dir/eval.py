from solver import Solver
from data_loader import get_loader
from configs import get_config

if __name__ == '__main__':
    config = get_config()

    data_loader = get_loader(
        batch_size=config.batch_size,
        is_train=False,
        data_dir=config.data_dir)

    solver = Solver(config, data_loader)
    solver.build(is_train=False)
    solver.eval()
