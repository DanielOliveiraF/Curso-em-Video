l = float(input('Largura da parede (m): '))
a = float(input('Altura da parede (m): '))
area = l * a
litros = area / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litros))