# from aiogram import Dispatcher
#
# from .antispam_middleware import Antispam
# from .callback_middleware import CallbackMiddleware
# from .check_role_middleware import CheckRoleMiddleware
# from .scheduler_middleware import SchedulerMiddleware
#
#
# def set_middleware(dp: Dispatcher):
#     dp.message.outer_middleware.register(CheckRoleMiddleware())
#     dp.update.middleware.register(SchedulerMiddleware(scheduler=CommonConfig.scheduler))
#     dp.message.middleware.register(Antispam(storage=CommonConfig.red_storage))
#     dp.callback_query.outer_middleware.register(CallbackMiddleware(storage=CommonConfig.red_storage))
