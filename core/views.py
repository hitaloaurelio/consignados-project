from django.shortcuts import render

# Create your views here.
from . import views
from django.http import JsonResponse
from core.models import Hospital,Medico,Consignado,Material,Empresa,CustomUser,SaidaAvulsa,ItensSaida

def index(request):

    # customUser = CustomUser.objects.get(id=request.user.id)
    empresa = request.user.empresa

    # Filtrar todas as consignações associadas à empresa do usuário
    # consignacoes_da_empresa = Consignado.objects.filter(empresa=empresa)  

    # user = request.user
    # print("Vendedora logada: ", user.first_name)
    # # Iterar sobre todas as consignações da empresa
    # for consignacao in consignacoes_da_empresa:
    #     print(" ")
    #     print("Vendedora da consignção: ", consignacao.vendedor.first_name)
    #     print("consignacao da data: ", consignacao.data)
    #     print("consignacao da medico: ", consignacao.medico)
    #     print("consignacao da paciente: ", consignacao.paciente)
    #     print("consignacao da hospital: ", consignacao.hospital)
    #     print("-------------------------")

    # # Recuperar materiais associados a esta consignação
    #     materiais_da_consignacao = consignacao.material.all()
    #     if not materiais_da_consignacao:
    #         print(" Consignado sem material cadastrado ")


    #     for material in materiais_da_consignacao:
    #         print("MATERIAS: ", material.nome)
    #     print("-------------------------")



    saida_avulsa = SaidaAvulsa.objects.filter(empresa=empresa)  
    for saida in saida_avulsa:
        print(" ")
        print(" ")
        print("Saida Vendedor nome: ", saida.vendedor.first_name)
        print("Saida data: ", saida.data)
        print("Saida da medico: ", saida.medico)
        print("Saida da paciente: ", saida.paciente)
        print("Saida da hospital: ", saida.hospital)
        
        itens = ItensSaida.objects.filter(saidaAvulsa=saida)
        for item in itens:
            print("-------------------------")
            print("Nome material: ",item.material)
            print("quantidade: ",item.quantiade)
            print("Lote: ",item.material.lote)
            print(" ")
           


              
    return JsonResponse({'message': 'OK'}, status=200)