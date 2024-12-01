from src.entity.Text2Analyze import Text2Analyze

text = '''Quince días después del terrible crimen, un hombre me abordó al salir de la biblioteca. Parecía un méndigo cuando lo miré: vestía con harapos y las arrugas de su rostro reflejaban con sinceridad el hambre y las dolencias de las que se quejó para que me compadeciera de su situación. Muchas veces yo carecía de dinero, pero nunca de buenas intenciones. Le invité a cenar con los vales que la escuela me facilitaba como parte de mi beca. Compré dos órdenes de carne deshebrada que comimos en una banca del parque frente a la cuarta avenida.
Aunque no recuerdo bien los hechos, haré mi mejor esfuerzo por exponerlos de la forma más fiel posible. Los hechos que a continuación narro desencadenarían el declive de Elker y, quizás, del reino mismo.'''
txt = Text2Analyze(text)
print("Word count list: ", txt.word_count_list())
print("Pause positions: ", txt.pause_positions())