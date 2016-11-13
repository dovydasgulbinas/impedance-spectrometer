classdef IVConverter < handle
    %DiffAmp Class abstracting the control of differential amplifier
    %   Detailed explanation goes here
%%%%%%%%% Kai prijungta LF, HF fb ir kal varza 1 kom, kai prijungta HF LF
%%%%%%%%%varzos 1 M (A. Kezionis)
    properties (Access = private)
        interface;
        addr;
        regIOA = 18;
        regIOB = 19;
        regDirA = 0;
        regDirB = 1;
    end
    
    properties (Access = public)
        resistor = 4;           % Resistors, ranging from 1 to 11. Also determines range variable.
        filter = 1;             % Filters, ranging from 1 to 4.
        range = 'HF';           % Range is determined by the chosen resistor.
        mode = 'MEAS';          % 'MEAS' for measurement and 'CAL' for calibration modes.
        attenuator = 'ON';      % Signal, coming from the generator, can be attenuated. Variable is either 'ON' or 'OFF'.
        gain = 1.7;             % Available gains after I-V conversion are 1.7 and 6.8.
    end
    
    methods (Access = private)        
        function write(self, register, bits)
            code = self.interface.WriteByteByte(self.addr, register, bits);
            if code == 0
                disp('IV Converter I2C write error.');
            end
        end
        
        function res = read(self, register)
            self.interface.Write(self.addr, [register], 1, false);
            [code, res] = self.interface.ReadByte(self.addr);
            if code == 0
                disp('IV Converter I2C read error.');
            end                
        end
        
        function res = setbits(self, bits, pattern)
            pattern = fliplr(pattern);
            mask = uint8(bin2dec(num2str(pattern)));
            res = bitor(bits, mask);
        end
        
        function [regA, regB] = generateRegisters(self)
            regA = 0;
            regB = 0;
            
            % resistors
            switch self.resistor
                % HF
                case 5
                    regB = self.setbits(regB, [0 0 0 0 0 0 0 1]);
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                case 4
                    regB = self.setbits(regB, [0 0 0 0 0 0 1 0]);
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                case 3
                    regB = self.setbits(regB, [0 0 0 0 0 1 0 0]);
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                case 2
                    regB = self.setbits(regB, [0 0 0 0 1 0 0 0]);
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                case 1
                    regB = self.setbits(regB, [0 0 0 1 0 0 0 0]);
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                case 6
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                    % no bits set for permanently connected resistors
                % LF
                case 7
                    regA = self.setbits(regA, [0 0 0 0 0 0 0 1]);
                    regB = self.setbits(regB, [0 0 0 0 1 0 0 0]);
                case 8
                    regA = self.setbits(regA, [0 0 0 0 0 0 1 0]);
                    regB = self.setbits(regB, [0 0 0 0 1 0 0 0]);
                case 9
                    regB = self.setbits(regB, [0 1 0 0 1 0 0 0]);
                case 10
                    regB = self.setbits(regB, [0 0 1 0 1 0 0 0]);
                case 11
                    regB = self.setbits(regB, [0 0 0 0 1 0 0 0]);
                    % no bits set for permanently connected resistors
            end
                    
            % filters
            switch self.filter
                case 4
                    regA = self.setbits(regA, [0 1 0 1 0 0 0 0]);
                case 2
                    regA = self.setbits(regA, [0 1 0 0 0 0 0 0]);
                case 3
                    regA = self.setbits(regA, [0 0 0 1 0 0 0 0]);
                case 1
                    % no bits set for position 4
            end
            
            % mode
            if strcmp(self.mode, 'MEAS')
                if strcmp(self.range, 'LF')
                    regA = self.setbits(regA, [0 0 0 0 0 1 0 0]);
                    regB = self.setbits(regB, [1 0 0 0 0 0 0 0]);
                elseif strcmp(self.range, 'HF')
                    regA = self.setbits(regA, [1 0 0 0 0 1 0 0]);
                end
            elseif strcmp(self.mode, 'CAL')
                if strcmp(self.range, 'LF')
                    regB = self.setbits(regB, [1 0 0 0 0 0 0 0]);                
                elseif strcmp(self.range, 'HF')
                    regA = self.setbits(regA, [1 0 0 0 0 0 0 0]);
                end
            end % no bits are set for HF measurement
                
            % attenuator
            if strcmp(self.attenuator, 'ON')
                regA = self.setbits(regA, [0 0 1 0 0 0 0 0]);
            end % bit is not set for 'OFF'
                
            % gain
            if self.gain == 6.8
                regA = self.setbits(regA, [0 0 0 0 1 0 0 0]);
            end % bit is not set for 1.7
        end
        
        function [regA, regB] = getRegisters(self)
            regA = self.read(self.regIOA);
            regB = self.read(self.regIOB);
        end
        
        function writeRegisters(self)
            self.write(self.regDirA, uint8(bin2dec(num2str([0 0 0 0 0 0 0 0]))));
            self.write(self.regDirB, uint8(bin2dec(num2str([0 0 0 0 0 0 0 0]))));
            [newRegA, newRegB] = self.generateRegisters();
            %[regA, regB] = self.getRegisters();
           % newRegA, newRegB
            %if newRegA ~= regA
                self.write(self.regIOA, newRegA);
           % end
           % if newRegB ~= regB
                self.write(self.regIOB, newRegB);
           % end
        end
    end

    methods
        function set.resistor(self, value)
            switch value
                % HF
                case 1
                    self.resistor = value;
                    self.range = 'HF';
                case 2
                    self.resistor = value;
                    self.range = 'HF';
                case 3
                    self.resistor = value;
                    self.range = 'HF';
                case 4
                    self.resistor = value;
                    self.range = 'HF';
                case 5
                    self.resistor = value;
                    self.range = 'HF';
                case 6
                    self.resistor = value;
                    self.range = 'HF';
                % LF
                case 7
                    self.resistor = value;
                    self.range = 'LF';
                case 8
                    self.resistor = value;
                    self.range = 'LF';
                case 9
                    self.resistor = value;
                    self.range = 'LF';
                case 10
                    self.resistor = value;
                    self.range = 'LF';
                case 11
                    self.resistor = value; 
                    self.range = 'LF';                   
                otherwise
                    disp('IVConverter: Invalid resistor index specified. Value was not modified.');
            end
        end
        
        function set.gain(self, value)
            f = true;
            if value == 1.7
                self.gain = value;
            elseif value == 6.8
                self.gain = value;
            else
                disp('IVConverter: Invalid gain specified. Value was not modified.');
                f = false;
            end
            if f               
                self.writeRegisters();
            end
        end
        
        function set.filter(self, value)
            f = true;
            switch value
                case 1
                    self.filter = value;
                case 2
                    self.filter = value;
                case 3
                    self.filter = value;
                case 4
                    self.filter = value;
                otherwise
                    disp('IVConverter: Invalid filter index specified. Value was not modified.');
                    f = false;
            end
            if f               
                self.writeRegisters();
            end
        end
        
        function set.attenuator(self, value)
            f = true;
            if strcmp(value, 'ON')
                self.attenuator = 'ON';
            elseif strcmp(value, 'OFF')
                self.attenuator = 'OFF';
            else
                disp('IVConverter: Attenuator can only be "ON" or "OFF". Value was not modified.');      
                f = false;
            end            
            if f               
                self.writeRegisters();
            end
        end
        
        function set.mode(self, value)
            f = true;
            if strcmp(value, 'MEAS')
                self.mode = 'MEAS';
            elseif strcmp(value, 'CAL')
                self.mode = 'CAL';
            else
                disp('IVConverter: Mode can only be "CAL" or "MEAS". Value was not modified.');     
                f = false;
            end
            if f               
                self.writeRegisters();
            end
        end
        
        function set.range(self, value)
            f = true;
            if strcmp(value, 'HF')
                self.range = 'HF';
            elseif strcmp(value, 'LF')
                self.range = 'LF';
            else
                disp('IVConverter: Range can only be "HF" or "LF". Value was not modified.');     
                f = false;
            end
            if f               
                self.writeRegisters();
            end
        end
    end
    
    methods (Access = public)
        function self = IVConverter(address, interface)
            self.interface = interface;
            self.addr = address;
            
            % Set output direction and default values
            self.writeRegisters();
        end
    end
end