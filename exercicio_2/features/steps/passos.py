from behave import given, when, then
from Deque import Deque

@given(u'o tamanho da estrutura que é {tamanho:d}')
def step_impl(context, tamanho):
    context.tamanho = tamanho


@when(u'crio um deque')
def step_impl(context):
   context.deque = Deque(context.tamanho)


@then(u'tenho um deque com capacidade para armazenar {elementos:d} elementos')
def step_impl(context, elementos):
    assert context.deque.tamanho == elementos


@then(u'uma estrutura esta vazia')
def step_impl(context):
    assert context.deque.empty is True


@given(u'que eu tenho um deque')
def step_impl(context):
    context.deque = Deque(context.tamanho)


@when(u'insiro, no final da estrutura, o valor {valor}')
def step_impl(context, valor):
    context.deque.push_back(valor)


@then(u'a estrutura nao esta vazia')
def step_impl(context):
   assert context.deque.empty is False


@then(u'o elemento na frente da estrutura tem o valor {valor}')
def step_impl(context, valor):
    assert context.deque.peek_front().dado == valor


@when(u'insiro, no final da estrutura, os valores {lista}')
def step_impl(context, lista):
    print(lista)
    assert lista == 0

@then(u'o elemento no final da estrutura tem o valor {valor}')
def step_impl(context, valor):
    assert context.deque.peek_back().dado == valor


@given(u'este deque tem elementos, inseridos no final, [ 1 , 3 , 5 , 7 ]')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given este deque tem elementos, inseridos no final, [ 1 , 3 , 5 , 7 ]')
    pass



