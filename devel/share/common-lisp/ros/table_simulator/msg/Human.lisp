; Auto-generated. Do not edit!


(cl:in-package table_simulator-msg)


;//! \htmlinclude Human.msg.html

(cl:defclass <Human> (roslisp-msg-protocol:ros-message)
  ((activateRobot
    :reader activateRobot
    :initarg :activateRobot
    :type cl:fixnum
    :initform 0)
   (humanIsReady
    :reader humanIsReady
    :initarg :humanIsReady
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Human (<Human>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Human>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Human)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name table_simulator-msg:<Human> is deprecated: use table_simulator-msg:Human instead.")))

(cl:ensure-generic-function 'activateRobot-val :lambda-list '(m))
(cl:defmethod activateRobot-val ((m <Human>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:activateRobot-val is deprecated.  Use table_simulator-msg:activateRobot instead.")
  (activateRobot m))

(cl:ensure-generic-function 'humanIsReady-val :lambda-list '(m))
(cl:defmethod humanIsReady-val ((m <Human>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader table_simulator-msg:humanIsReady-val is deprecated.  Use table_simulator-msg:humanIsReady instead.")
  (humanIsReady m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Human>) ostream)
  "Serializes a message object of type '<Human>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'activateRobot)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'humanIsReady)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Human>) istream)
  "Deserializes a message object of type '<Human>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'activateRobot)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'humanIsReady)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Human>)))
  "Returns string type for a message object of type '<Human>"
  "table_simulator/Human")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Human)))
  "Returns string type for a message object of type 'Human"
  "table_simulator/Human")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Human>)))
  "Returns md5sum for a message object of type '<Human>"
  "23987e0baa57fd119547d559cbd31dd5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Human)))
  "Returns md5sum for a message object of type 'Human"
  "23987e0baa57fd119547d559cbd31dd5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Human>)))
  "Returns full string definition for message of type '<Human>"
  (cl:format cl:nil "uint8 activateRobot~%uint8 humanIsReady~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Human)))
  "Returns full string definition for message of type 'Human"
  (cl:format cl:nil "uint8 activateRobot~%uint8 humanIsReady~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Human>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Human>))
  "Converts a ROS message object to a list"
  (cl:list 'Human
    (cl:cons ':activateRobot (activateRobot msg))
    (cl:cons ':humanIsReady (humanIsReady msg))
))
