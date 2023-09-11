from functools import wraps
#def soma_dois_inteiros(x, y):
	#if all(isinstance(valores, int) for valores in [x, y]):
		#return x + y


# Uso de decorators.

def validacao_da_soma_de_dois_inteiros(funcao):
	# A variável "funcao", é livre dentro do escopo de "validacao_da_soma_de_dois_inteiros".
	
	def interna(*args):
		if all(isinstance(valores, int) for valores in args):
			print(f'Log de {funcao.__name__} args: {args}')
			# Retornará a função que chamou "validacao_da_soma_de_dois_inteiros", 
			# com os argumentos passados por ela.
			# "soma" chama "validacao_da_soma_de_dois_inteiros", que retorna "soma" com seus argumentos.
			return funcao(*args)
		else:
			# callback.
			return 'Deu ruim'
	return interna    


def validacao_do_tipo_inteiro(type):
    # A variável "type", é livre dentro do escopo de "validacao_do_tipo_inteiro"
    
    def validacao_da_soma_de_dois_inteiros(funcao):
        # A variável "funcao", é livre dentro do escopo de "validacao_da_soma_de_dois_inteiros".
        
        @wraps(funcao) # Leva o escopo da função que é decorada por "validacao_do_tipo_inteiro" para fora, melhor para debugar
        def interna(*args, **kwargs):
            if all(isinstance(valores, type) for valores in args):
                print(f'Log de {funcao.__name__} args: {args}')
                # Retornará a função que chamou "validacao_da_soma_de_dois_inteiros", 
                # com os argumentos passados por ela.
                ## "soma" chama "validacao_da_soma_de_dois_inteiros", que retorna "soma" com seus argumentos.
                return funcao(*args)
            else:
                # callback.
                return 'Deu ruim'
        return interna
    return validacao_da_soma_de_dois_inteiros


@validacao_do_tipo_inteiro(int)
@validacao_da_soma_de_dois_inteiros
def soma(x, y):
    return x + y


soma = soma(2, 2)

print(f'Resultado da soma: {soma}')
