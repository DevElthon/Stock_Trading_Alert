# Stock_Trading_Alert
No mundo das ações é necessário estar o tempo todo de olho nos preços. Pensando nisso, criei esse programa para verificar e comparar os preços atuais de determinada empresa com os preços passados.

A empresa alvo para esse programa, será a Tesla Inc, porém, funciona com qualquer empresa presente na base de dados. A base de dados é obtida através da API "https://www.alphavantage.co/query". Obtendo as informações através da biblioteca "requests" utilizando a API, podemos criar uma comparação. 

Após a comparação ser realiza, dependendo da porcentagem, o programa irá disparar um alerta via SMS utilizando a biblioteca "twilio". A mensagem enviada no SMS será referente a notícias sobre a alteração nos preços da empresa de obtidas através da API "https://newsapi.org/v2/everything".

O programa pode ser hospedado no pythonanywhere: https://www.pythonanywhere.com para que o mesmo possa rodar todos os dias em um horário específico. Porém, para hospedar o mesmo algumas alterações devem ser feitas no "twilio" pois o mesmo precisa de simular um servidor e um cliente como parâmetro para rodar em nuvem.
