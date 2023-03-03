require 'logger'

module Citronella
  def self.logger(logger, class_name, function_name, name)
    if logger
      Logger.new(STDOUT, level: Logger::INFO).info(
        "#{class_name} => #{function_name} => #{name}")
    end
  end
end
