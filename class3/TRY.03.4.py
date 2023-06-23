def func(name,job):
    print(name,"is a"job)
    func(name = "bob",job = 'developer')
    func(job="developer",name= "bob")