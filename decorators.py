# log function call
import time


def log_function_call(func):
    def show_details(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result

    return show_details


# @log_function_call
def add(a, b):
    return a + b


add(5, 3)


# Time measurement decorator
def measure_time(func):
    def measure(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution = end - start
        print(f"{func.__name__} executed in {execution:.3f} seconds")
        return result

    return measure


# @measure_time
def slow_function():
    time.sleep(1)


# slow_function()
# Access control decorator
def requires_role(role):
    def decorator(func):
        def access(*args, **kwargs):
            user_role = kwargs.get("user_role")
            if user_role == role:
                print("Access granted")
                return func()
            elif user_role == "guest":
                print("Access denied")
            else:
                print("Sorry,who are you?")

        return access
    return decorator


# @requires_role('admin')
def sensitive_operation():
    print("Sensitive operation performed.")


# sensitive_operation(user_role="admin")




