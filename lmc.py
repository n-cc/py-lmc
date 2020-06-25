class LMC:
    def __init__(self):
        self.mem = []
        self.box = 0
        self.ptr = 0

        self.instructions = {
            1 : self.add,
            2 : self.sub,
            3 : self.sto,
            5 : self.lda,
            6 : self.br,
            7 : self.brz,
            8 : self.brp,
            9 : self.ctl,
            0 : self.zzz,
        }

        self.verbose = True

    # LMC instructions

    def add(self, input):
        log('Adding {} to address {} with value {}'.format(self.box, input, self.mem[input]))
        self.box += self.mem[input]

    def sub(self, input):
        log('Subtracting {} from address {} with value {}'.format(self.box, input, self.mem[input]))
        self.box -= self.mem[input]

    def sto(self, input):
        log('Storing {} at address {}'.format(self.box, input))
        self.mem[input] = self.box

    def lda(self, input):
        log('Loading {} from address {} into box'.format(self.mem[input], input))
        self.box = self.mem[input]

    def br(self, input):
        log('Branching to {}'.format(input))
        self.ptr = input

    def brz(self, input):
        if self.box == 0:
            self.ptr = input

    def brp(self, input):
        if self.box >= 0:
            self.ptr = input

    def ctl(self, input):
        if input == 1:
            try:
                self.box == int(input('INPUT: '))
            except:
                raise NameError
        elif input == 2:
            print(str(self.box))

    def zzz(self, input):
        raise NameError

    # Functions

    def log(self, msg):
        if self.verbose:
            print(msg)

    def initram(self):
        self.mem = []
        for i in range(0, 100):
            self.mem.append(None)

    def run(self):
        while(True):
            data = self.mem[self.ptr]
            self.ptr += 1
            try:
                self.instructions[int(str(data)[:1])](int(str(data)[:]))
            except ValueError:
                continue
            except NameError:
                break
            if self.ptr > 99:
                break

    def dump(self):
        iter = 0
        for data in self.mem:
            iter += 1
            if data is not None:
                print('{}: {}'.format(str(iter), str(data)))

    def poke(self, addr, data):
        try:
            self.mem[addr] = data
            self.log('Poked {} with {}'.format(addr, data))
        except IndexError:
            print('Address out of bounds: ' + str(addr))

    def main(self):
        ret = 0
        self.initram()
        while(True):
            c = input('? ')
            try:
                addr = int(c.split(' ')[0])
                data = int(c.split(' ')[1])
                self.poke(addr, data)
            except ValueError:
                if c == "run":
                    self.run()
                elif c == "dump":
                    self.dump()
                elif c == "reset":
                    self.initram()
                elif c == "exit":
                    break
                else:
                    print('addr data OR run|dump|reset')
            except IndexError:
                print('Incomplete command')
        return(ret)

if __name__ == "__main__":
    LMC = LMC()
    ret = LMC.main()
    quit(ret)
