try:
    fh = open("D:/Git/Class-assignment-29/testfile", "w")
    try:
        fh.write("����һ�������ļ������ڲ����쳣!!")
    finally:
        print "�ر��ļ�"
        fh.close()
except IOError:
    print "Error: û���ҵ��ļ����ȡ�ļ�ʧ��"
