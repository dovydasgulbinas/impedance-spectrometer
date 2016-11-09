classdef I2C < handle
    methods
        function self = I2C()
        end
        function res = WriteByteByte(self, addr, register, bits)
            res = 0;
        end
        function res = Write(self, addr, register, bit, logic)
            res = 0;
        end
        function [code, res] = ReadByte(self, addr)
            code = 0;
            res = 1;
        end
    end
end

