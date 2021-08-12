import logging
def get_logger(name="py36",
               logger_level="DEBUG",
               handler_level="DEBUG",
               file=None,
               file_level="INFO",
               fmt_str="%(asctime)s-%(levelname)s:%(name)s:%(message)s-%(filename)s-line%(lineno)s"):
    logger = logging.getLogger(name)   #获取日志收集器
    logger.setLevel(logger_level)    #设置日志收集器等级
    fmt = logging.Formatter(fmt_str)  # 设置日志处理器格式
    handler =logging.StreamHandler()   #获取日志处理器
    handler.setLevel(handler_level)    #设置日志处理器等级
    logger.addHandler(handler)     #处理器添加到收集器上
    handler.setFormatter(fmt)   #把日志处理器格式添加到日志处理器上
    if file:
        file_handler = logging.FileHandler("review.log",encoding="utf-8")     #获取文件处理器
        file_handler.setLevel("INFO")     #设置文件处理器等级
        logger.addHandler(file_handler)     #把文件处理器添加到日志收集器上
        file_handler.setFormatter(fmt)
    return logger
if __name__ == '__main__':
    logger = get_logger(file="review.log")
    logger.debug("222")
    logger.info("111")
    logger.error("333")
    

