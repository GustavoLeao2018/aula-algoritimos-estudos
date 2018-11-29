from behave import given, when, then
from Deque import Deque

@given(u'o tamanho da estrutura que é {tamanho:d}')
def given_tamanho(context, tamanho):
    context.tamanho = tamanho


@when(u'crio um deque')
def when_create_deque(context):
   context.deque = Deque(context.tamanho)


@then(u'tenho um deque com capacidade para armazenar {elementos:d} elementos')
def then_tamanho_elements_is_equals(context, elementos):
    assert context.deque.tamanho == elementos


@then(u'uma estrutura esta vazia')
def then_is_void(context):
    assert context.deque.empty is True


@given(u'que eu tenho um deque')
def given_a_deque(context):
    context.deque = Deque(10)


@when(u'insiro, no final da estrutura, o valor {valor}')
def when_push_back_value(context, valor):
    context.deque.push_back(valor)


@then(u'a estrutura nao esta vazia')
def then_is_not_void(context):
   assert context.deque.empty is False


# TODO: Este está com erro
@then(u'o elemento na frente da estrutura tem o valor {valor}')
def then_peeek_front(context, valor):
    assert context.deque.peek_front().dado is valor


@when(u'insiro, no final da estrutura, os valores [ 1 , 2 , 3 , 4 ]')
def when_push_itens(context):
    lista_acrescentar = [1, 2, 3, 4]
    for item in lista_acrescentar:
        context.deque.push_back(item)

@then(u'o elemento no final da estrutura tem o valor {valor}')
def then_final_is_value(context, valor):
    assert context.deque.peek_back().dado is valor


@given(u'este deque tem elementos, inseridos no final, [ 1 , 3 , 5 , 7 ]')
def given_values_to_list(context):
    lista_acrescentar = [ 1,3,5,7 ]
    for item in lista_acrescentar:
        context.deque.push_back(item)

@when(u'insiro, no início da estrutura, os valores [4, 3, 2, 1]')
def when_push_front_values(context):
    lista_acrescentar = [ 4, 3, 2, 1 ]
    for item in lista_acrescentar:
        context.deque.push_front(item)


@given(u'este deque tem os elementos, inseridos no final, {lista}')
def given_push_front_itens(context, lista):
    lista_acrescentar = list(lista)
    for item in lista_acrescentar:
        context.deque.push_front(item)


@when(u'insiro, no início da estrutura, o valor {valor}')
def when_push_front_value(context, valor):
    context.deque.push_front(valor)


@when(u'apago, no final da estrutura')
def when_pop_back_a_value(context):
    context.deque.pop_back()
