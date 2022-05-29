# Первая строка содержит количество предметов  1≤n≤10^3 и вместимость рюкзака
#  0≤W≤2⋅10^6. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6  и объём 0<wi≤2⋅10^6 предмета (n, W, ci, wi — целые числа).
#  Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом
#  пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
#
def max_objects_in_backpack(volume_of_backpack, cost, volume, cost_per_kilo):
    sorted_cost = [x for _, x in sorted(zip(cost_per_kilo, cost))]
    sorted_volume = [x for _, x in sorted(zip(cost_per_kilo, volume))]
    cost_per_kilo.sort()
    print('sorted cost = {}, sorted_volume = {}'.format(sorted_cost, sorted_volume))
    print('cost per kilo = {}'.format(cost_per_kilo))
    total_cost = 0
    total_volume = 0
    if volume_of_backpack == 0:
        return 0.000
    if volume_of_backpack <= sorted_volume[-1]:
        return '{:.3f}'.format(cost_per_kilo[-1] * volume_of_backpack)
    for i in reversed(range(len(cost_per_kilo))):
        if volume_of_backpack > total_volume:
            current_free_volume = volume_of_backpack - total_volume
            if current_free_volume >= sorted_volume[i]:
                total_volume += sorted_volume[i]
                total_cost += sorted_cost[i]
            else:
                total_cost += cost_per_kilo[i] * current_free_volume
                break
    return f"{total_cost:.3f}"


    #return '{:.3f}'.format(x)

n, backpack_volume = map(int, input().split())
cost = []
volume = []
cost_per_kilo = []
for i in range(n):
    tc, twi = map(int, input().split())
    cost.append(tc)
    volume.append(twi)
    cost_per_kilo.append(tc/twi)
print(max_objects_in_backpack(backpack_volume, cost, volume, cost_per_kilo))

#not my but beautiful variant
# n, backpack_volume = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(n)]
# items.sort(key=lambda x: x[0]/x[1], reverse=True)
# weight, cost = 0, 0
# for item in items:
#     cur_weight = min(item[1], backpack_volume - weight)
#     if weight + cur_weight > backpack_volume:
#         break
#     cost += (item[0] / item[1]) * cur_weight
#     weight += cur_weight
#
# print("%.3f" % cost)
#