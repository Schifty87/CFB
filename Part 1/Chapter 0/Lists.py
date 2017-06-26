myList = [1, 2, 3, ['hello', 'there'], 42, 47];
print len(myList);
print myList[5];
print myList[len(myList)-1];
print myList[3];

list1 = [1, 2, 3];
list2 = [4, 5, 6];
list3 = list1 + list2;
print list3;

list4 = list1;
list4.append(list2);
print list4;

list5 = list1[0:2];
list5.append(list2);
list5.append(list1[2]);
list5.append(list2[0]);
print list5;