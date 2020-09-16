NAME := rpn
INCLUDES = -I includes
CFLAGS := -Wall -Wextra -Werror

SRCS = rpn.c
OBJ_DIR = objects/
OBJ_LST = $(patsubst %.c, %.o, $(SRCS))
OBJ	= $(addprefix $(OBJ_DIR), $(OBJ_LST))

all: $(NAME)

$(NAME):  $(OBJ_DIR) $(OBJ)
	gcc $(CFLAGS) $(OBJ) $(HEADERS) -o $(NAME)

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

objects/%.o : %.c
	gcc $(CFLAGS) -c $(INCLUDES) $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean $(NAME)

.PHONY: all clean fclean re


